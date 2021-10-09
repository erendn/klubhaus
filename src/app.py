from .chatroom import chatroom
from .command import command
from .state import state
from src.utils import *


class app:
    """ Application class to run the program. """

    def __init__(self):

        # Program variables
        self.con = None
        self.state = state.IDLE

        # Default socket configs
        self.host = "localhost"
        self.port = 5000
        self.backlog = 5

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

        if self.con:
            self.print_warning("You can only host 1 chat room at the same time.")
        else:
            username = get_input("Enter username: ")
            port = get_input("Enter the port number: ")
            self.con = chatroom(username=username,
                                port=port,
                                is_host=True)
            self.state = state.HOSTING


    def connect(self):
        """ Connect to a chat room. """

        if self.con:
            self.print_warning("You can only connect to 1 chat room at the same time.")
        else:
            username = get_input("Enter username: ")
            port = get_input("Enter the port number: ")
            self.con = chatroom(username=username,
                                port=port)
            self.state = state.CONNECTED


    def disconnect(self):
        """ Disconnect from the chatroom. """

        if self.con:
            del self.con
            self.con = None
        self.state = state.IDLE


    def exit(self):
        """ Exit the program. """

        self.disconnect()


    def print_ui(self):
        """ Print the console UI of the program. """

        clear_screen()
        print_banner()
        self.print_commands()
        self.print_warning()


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