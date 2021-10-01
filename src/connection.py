import socket
from time import sleep
from threading import Thread
import pyaudio
from .utils import *

# Default sound configs
CHUNK = 1024
FORMAT = pyaudio.paInt16
CHANNELS = 2
RATE = 44100


class connection:
    """ Peer-to-peer connection class. """

    def __init__(self, username, host="localhost", port=0, is_host=False, connect_limit=2):

        self.username = username

        # Create a socket for connections
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        if is_host:
            self.sock.bind((host, port))
            self.sock.listen(1)
        else:
            self.sock.connect((host, port))
        # Set the socket non-blocking to prevent a user blocking others' voice
        self.sock.setblocking(False)

        self.connections = []
        if not is_host:
            self.connections.append({
                "socket": self.sock,
                "username": None,
            })
        self.is_host = is_host
        self.is_open = True
        self.connect_limit = connect_limit

        self.setup_sound()

        # Run the threads
        if is_host:
            con_thread = Thread(target=self.accept_connections, daemon=True)
            con_thread.start()
        in_thread = Thread(target=self.send_sound, daemon=True)
        in_thread.start()
        out_thread = Thread(target=self.receive_sound, daemon=True)
        out_thread.start()


    def __del__(self):

        self.is_open = False
        for con in self.connections:
            con["socket"].close()
        self.sock.close()
        self.input.close()
        self.output.close()
        self.pa.terminate()


    def connect(self):
        """ Connect a new user to the call. """

        sock, _ = self.sock.accept()
        self.connections.append({
            "socket": sock,
            "username": None,
        })


    def disconnect(self, username):
        """ Disconnect a user from the call. """

        for con in self.connections:
            if con["username"] == username:
                con["socket"].close()
                self.connections.remove(con)
                break


    def accept_connections(self):
        """
        Wait and accept new connections.
        This method should be run by a thread.
        """

        while self.is_open:
            if len(self.connections) < self.connect_limit:
                try:
                    self.connect()
                except BlockingIOError:
                    sleep(1)
                    continue


    def setup_sound(self):
        """ Setup sound input and output streams. """

        self.pa = pyaudio.PyAudio()
        # Sound input
        self.input = self.pa.open(format=FORMAT,
                                  channels=CHANNELS,
                                  rate=RATE,
                                  input=True,
                                  frames_per_buffer=CHUNK)
        # Sound output
        self.output = self.pa.open(format=FORMAT,
                                   channels=CHANNELS,
                                   rate=RATE,
                                   output=True)


    def sound_input(self):
        """ Return a chunk of sound from the input stream. """

        return self.input.read(CHUNK)


    def sound_output(self, frame):
        """ Write a chunk of sound to the output stream. """

        self.output.write(frame)


    def send_sound(self):
        """
        Send input stream to all connected users.
        This method should be run by a thread.
        """

        while self.is_open:
            frame = self.sound_input()
            for con in self.connections:
                try:
                    con["socket"].sendall(frame)
                except socket.error:
                    continue


    def receive_sound(self):
        """
        Receive output stream from all connected users.
        This method should be run by a thread.
        """

        while self.is_open:
            for con in self.connections:
                try:
                    frame = con["socket"].recv(CHUNK)
                    self.sound_output(frame)
                except socket.error:
                    continue