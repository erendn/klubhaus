import socket
from pyngrok import ngrok
from .protocol import protocol
from .settings import SETTINGS


class server_socket:
    """ Server socket class to accept new users to chatrooms. """

    def __init__(self, host, port, backlog=1):

        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.bind((host, port))
        self.address = self.sock.getsockname()
        self.sock.listen(backlog)
        self.sock.setblocking(False)
        self.start_ssh_tunnel()


    def accept(self, username, address, other_prots):
        """ Accept a new user to the chatroom via protocol. """

        try:
            sock, _ = self.sock.accept()
            prot = protocol(sock, True)
            prot.establish(username, address, other_prots)
            return prot
        except socket.error:
            return


    def close(self):
        """ Close the server socket. """

        self.close_ssh_tunnel()
        self.sock.close()


    def start_ssh_tunnel(self):
        """ Start the SSH tunnel via ngrok. """

        self.tunnel = ngrok.connect(
            addr=self.address[1],
            proto="tcp",
            options={"region": SETTINGS["tunnel_region"]}
        )
        url = self.tunnel.public_url.split("//")[1]
        self.public_address = tuple(url.split(":"))


    def close_ssh_tunnel(self):
        """ Close the SSH tunnel of ngrok. """

        ngrok.disconnect(self.tunnel.public_url)