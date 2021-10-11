import json
import socket


class protocol:

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
        """"""

        self.sock.connect((host, port))


    def establish(self, username, address, user_addresses=None):
        """"""

        user_addresses = None
        if not self.ready:
            # If this isn't host, send setup info first
            if not self.is_host:
                self.send_setup_info(username, address)
                user_addresses = self.recv_setup_info()
            else:
                self.recv_setup_info()
                self.send_setup_info(username, address, user_addresses)
            self.sock.setblocking(False)
            self.ready = True
        return user_addresses


    def close(self):
        """"""

        self.sock.close()


    def send_setup_info(self, username, address, user_addresses=None):
        """"""

        data = {
            "username": username,
            "address": address,
        }
        if user_addresses:
            data["hosts"] = [x[0] for x in user_addresses]
            data["ports"] = [x[1] for x in user_addresses]
        data = json.dumps(data).encode("utf-8")
        self.sock.sendall(data)


    def recv_setup_info(self):
        """"""

        from .chatroom import CHUNK
        data = self.sock.recv(CHUNK)
        data = json.loads(data)
        self.username = data["username"]
        self.address = data["address"]
        if "hosts" in data.keys():
            user_addresses = []
            for i in range(len(data["hosts"])):
                user_addresses.append((data["hosts"][i], data["ports"][i]))
            return user_addresses


    def send(self, data):
        """"""

        if self.ready:
            try:
                self.sock.sendall(data)
            except socket.error:
                return


    def recv(self):
        """"""

        if self.ready:
            try:
                from .chatroom import CHUNK
                return self.sock.recv(CHUNK)
            except socket.error:
                return