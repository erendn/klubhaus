from .chatroom import chatroom
from .command import command
from .state import state
from src.utils import *


class app:
    """ Application class to run the program. """

    def __init__(self):

        # Program variables
        self.room = None
        self.state = state.IDLE
        self.warning_msg = None


    def run(self):
        """ Run the program. """

        while True:
            self.print_ui()

            com = get_command()
            if com == command.NEW_CHATROOM:
                self.new_chat_room()
            elif com == command.CONNECT:
                self.connect()
            elif com == command.DISCONNECT:
                self.disconnect()
            elif com == command.EXIT:
                self.exit()
                break
            else:
                # TODO: Print warning message here
                continue


    def new_chat_room(self):
        """ Host a new chat room. """

        if self.room:
            self.print_warning("You can only host 1 chat room at the same time.")
        else:
            username = get_input("Enter username: ")
            self.room = chatroom(username=username)
            print("This program is listening to:")
            print(f"Host: {self.room.sock.address[0]}")
            print(f"Port: {self.room.sock.address[1]}")
            host = get_input("Enter your NAT tunnel host: ")
            port = get_input("Enter your NAT tunnel port: ")
            self.room.tunnel_address = (host, port)
            self.room.start_room()
            self.state = state.HOSTING


    def connect(self):
        """ Connect to a chat room. """

        if self.room:
            self.print_warning("You can only connect to 1 chat room at the same time.")
        else:
            username = get_input("Enter username: ")
            self.room = chatroom(username=username)
            print("This program is listening to:")
            print(f"Host: {self.room.sock.address[0]}")
            print(f"Port: {self.room.sock.address[1]}")
            host = get_input("Enter your NAT tunnel host: ")
            port = get_input("Enter your NAT tunnel port: ")
            self.room.tunnel_address = (host, port)
            host = get_input("Enter host to connect: ")
            port = get_input("Enter port to connect: ")
            self.room.connect(host, port)
            self.room.start_room()
            self.state = state.CONNECTED


    def disconnect(self):
        """ Disconnect from the chatroom. """

        if self.room:
            del self.room
            self.room = None
        self.state = state.IDLE


    def exit(self):
        """ Exit the program. """

        self.disconnect()


    def print_ui(self):
        """ Print the console UI of the program. """

        clear_screen()
        print_banner()
        self.print_info()
        self.print_commands()
        self.print_warning()


    def print_info(self):
        """"""

        if self.room:
            print("This program is listening to:")
            print(f"Host: {self.room.sock.address[0]}")
            print(f"Port: {self.room.sock.address[1]}")


    def print_commands(self):
        """ Print current commands. """

        table = []
        if self.state == state.IDLE:
            table.extend([
                ["new chatroom", "Host a new chatroom"],
                ["connect", "Connect to a host"]
            ])
        if self.state == state.HOSTING or self.state == state.CONNECTED:
            table.append(["disconnect", "Disconnect from the chatroom"])
        table.append(["exit", "Exit"])
        print_table(table)


    def print_warning(self, msg=None):
        """ Print a warning on the console. """

        # TODO: Print multiple warning messages
        if msg:
            self.warning_msg = msg

        if self.warning_msg:
            print()
            print("╔" + "═" * (len(self.warning_msg) + 4) + "╗")
            print("║  " + self.warning_msg + "  ║")
            print("╚" + "═" * (len(self.warning_msg) + 4) + "╝")
            print()

        if msg is None:
            self.warning_msg = None