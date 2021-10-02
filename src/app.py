from .connection import connection
from src.utils import *


class app:
    """ Application class to run the program. """

    def __init__(self):

        # Program variables
        self.con = None
        self.state = "idle"

        # Default socket configs
        self.host = "localhost"
        self.port = 5000
        self.backlog = 5

        self.warning_msg = None


    def run(self):
        """ Run the program. """

        while True:
            self.print_ui()

            command = get_command()
            if command == "new connection":
                self.new_connection()
            elif command == "connect":
                self.connect()
            elif command == "disconnect":
                self.disconnect()
            elif command == "exit":
                self.exit()
                break


    def new_connection(self):
        """ Host a new connection. """

        if self.con:
            self.print_warning("You can only host 1 connection at the same time.")
        else:
            username = get_input("Enter username: ")
            port = get_input("Enter the port number: ")
            self.con = connection(username=username,
                                  port=port,
                                  is_host=True)
            self.state = "hosting"


    def connect(self):
        """ Connect to a host. """

        if self.con:
            self.print_warning("You can only connect to 1 host at the same time.")
        else:
            username = get_input("Enter username: ")
            port = get_input("Enter the port number: ")
            self.con = connection(username=username,
                                  port=port)
            self.state = "connected"


    def disconnect(self):
        """ Disconnect the connection. """

        if self.con:
            del self.con
            self.con = None
        self.state = "idle"


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

        WIDE = 30
        print("\n╔═════╦" + "═" * (WIDE) + "╗")
        if self.state == "idle":
            print("║  N  ║ Host a new connection        ║")
            print("╠═════╬" + "═" * (WIDE) + "║")
            print("║  C  ║ Connect to a host            ║")
            print("╠═════╬" + "═" * (WIDE) + "║")
        if self.state == "hosting" or self.state == "connected ║":
            print("║  D  ║ Disconnect the connection    ║")
            print("╠═════╬" + "═" * (WIDE) + "║")
        print("║ Esc ║ Exit                         ║")
        print("╚═════╩" + "═" * (WIDE) + "╝\n")


    def print_warning(self, msg=None):
        """ Print a warning on the console. """

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