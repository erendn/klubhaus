import json
import socket
from .utils import *


class protocol:
    """ Protocol class to establish chatroom connections between clients. """

    def __init__(self, sock=None, is_host=False):

        if sock:
            self.sock = sock
        else:
            self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.is_host = is_host
        self.username = None
        self.address = None
        self.ready = False


    def connect(self, host, port):
        """ Connect to a chatroom server socket. """

        self.sock.connect((host, port))


    def establish(self, username, address, other_prots):
        """ Establish the protocol by exchanging information about chatroom users. """

        if not self.ready:
            # If this isn't host, send setup info first
            if not self.is_host:
                self.send_setup_info(username, address, other_prots)
                other_prots = self.recv_setup_info()
            else:
                self.recv_setup_info()
                self.send_setup_info(username, address, other_prots)
            self.sock.setblocking(False)
            self.ready = True
            return other_prots


    def close(self):
        """ Close the protocol's socket. """

        self.sock.close()


    def send_setup_info(self, username, address, other_prots):
        """ Send setup information for the protocol. """

        data = {
            "username": username,
            "address": address,
        }
        data["hosts"] = [x.address[0] for x in other_prots]
        data["ports"] = [x.address[1] for x in other_prots]
        data = json.dumps(data).encode("utf-8")
        self.sock.sendall(data)


    def recv_setup_info(self):
        """ Receive setup information for the protocol. """

        data = self.sock.recv(CHUNK)
        data = json.loads(data)
        self.username = data["username"]
        self.address = data["address"]
        if "hosts" in data.keys():
            user_addresses = []
            for i in range(len(data["hosts"])):
                user_addresses.append((data["hosts"][i], int(data["ports"][i])))
            return user_addresses


    def send(self, data):
        """ Send data through sockets. """

        if self.ready:
            try:
                self.sock.sendall(data)
            except socket.error:
                return


    def recv(self):
        """ Receive data through sockets. """

        if self.ready:
            try:
                return self.sock.recv(CHUNK)
            except socket.error:
                return