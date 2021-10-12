from time import sleep
from threading import Thread
import pyaudio
from .protocol import protocol
from .server_socket import server_socket
from .utils import *


class chatroom:
    """ Peer-to-peer chatroom class. """

    def __init__(self, username, host="localhost", port=0, room_size=2):

        self.username = username

        # Create a server_socket to accept new connections to the chatroom
        self.sock = server_socket(host, port)

        print("This program is listening to:")
        print(f"Host: {self.sock.address[0]}")
        print(f"Port: {self.sock.address[1]}")
        host = get_input("Enter your NAT tunnel host: ")
        port = get_input("Enter your NAT tunnel port: ")
        self.tunnel_address = (host, port)

        self.connections = []
        self.room_size = room_size
        self.is_open = True


    def __del__(self):

        self.is_open = False
        for con in self.connections:
            con.close()
        self.sock.close()
        self.input.close()
        self.output.close()
        self.pa.terminate()


    def connect(self, host, port):
        """ Connect to a chatroom through a user. """

        prot = protocol()
        prot.connect(host, port)
        prot.establish(self.username, self.tunnel_address)
        self.connections.append(prot)


    def start_room(self):
        """ Start the chatroom. """

        self.setup_sound()
        # Run the threads
        con_thread = Thread(target=self.accept_connections, daemon=True)
        con_thread.start()
        in_thread = Thread(target=self.send_sound, daemon=True)
        in_thread.start()
        out_thread = Thread(target=self.receive_sound, daemon=True)
        out_thread.start()


    def accept_connections(self):
        """
        Wait and accept new connections.
        This method should be run by a thread.
        """

        while self.is_open:
            if len(self.connections) < self.room_size - 1:
                prot = self.sock.accept(self.username, self.tunnel_address, self.connections)
                if prot:
                    self.connections.append(prot)
            sleep(1) # Don't overwhelm the CPU


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
                con.send(frame)


    def receive_sound(self):
        """
        Receive output stream from all connected users.
        This method should be run by a thread.
        """

        while self.is_open:
            for con in self.connections:
                frame = con.recv()
                if frame:
                    self.sound_output(frame)