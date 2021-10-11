import socket
from .protocol import protocol


class server_socket:
    """"""

    def __init__(self, host, port, backlog=1):

        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.bind((host, port))
        self.address = self.sock.getsockname()
        self.sock.listen(backlog)
        self.sock.setblocking(False)


    def accept(self, username, address, user_addresses=None):
        """"""

        try:
            sock, _ = self.sock.accept()
            prot = protocol(sock, True)
            prot.establish(username, address, user_addresses)
            return prot
        except socket.error:
            return


    def close(self):
        """"""

        self.sock.close()