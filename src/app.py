from .settings import *
from .chatroom import chatroom
from .command import command
from .state import state
from .utils import *


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

            if self.state == state.SETTINGS:
                self.settings_menu()
                continue

            com = get_command()
            if com == command.NEW_CHATROOM:
                self.new_chat_room()
            elif com == command.CONNECT:
                self.connect()
            elif com == command.DISCONNECT:
                self.disconnect()
            elif com == command.SETTINGS:
                self.settings_menu()
            elif com == command.EXIT:
                self.exit()
                break
            else:
                # TODO: Print warning message here
                continue


    def new_chat_room(self):
        """ Host a new chat room. """

        if self.state == state.IDLE:
            if self.room:
                self.print_warning("You can only host 1 chat room at the same time.")
            else:
                username = get_input("Enter username: ")
                self.room = chatroom(username)
                self.room.start_room()
                self.state = state.HOSTING


    def connect(self):
        """ Connect to a chat room. """

        if self.state == state.IDLE:
            if self.room:
                self.print_warning("You can only connect to 1 chat room at the same time.")
            else:
                username = get_input("Enter username: ")
                self.room = chatroom(username)
                host = get_input("Enter host to connect: ")
                port = get_input("Enter port to connect: ")
                self.room.connect(host, port)
                self.room.start_room()
                self.state = state.CONNECTED


    def disconnect(self):
        """ Disconnect from the chatroom. """

        if self.state == state.HOSTING or self.state == state.CONNECTED:
            if self.room:
                self.room.stop_room()
                self.room = None
            self.state = state.IDLE


    def settings_menu(self):
        """ Change settings of the app. """

        self.state = state.SETTINGS
        print_table(SETTINGS)

        com = get_input("Change setting (type 'back' to return): ")
        if com == "back":
            self.state = state.IDLE
            return

        if com == "tunnel_region":
            region = get_input("Enter the SSH tunnel region for ngrok: ")
            change_setting(com, region)

        if com == "audio_in_index" or com == "audio_out_index":
            print_audio_devices()
            index = get_input("Enter the device index: ")
            change_setting(com, index)


    def exit(self):
        """ Exit the program. """

        self.disconnect()


    ##################################################
    #                UI METHODS BELOW                #
    ##################################################


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
            text = "This program is listening to:\n" + \
                f"Host: {self.room.sock.address[0]}\n" + \
                f"Port: {self.room.sock.address[1]}"
            print_box(text)
            text = "Your NAT tunnel is:\n" + \
                f"Host: {self.room.sock.public_address[0]}\n" + \
                f"Port: {self.room.sock.public_address[1]}"
            print_box(text)


    def print_commands(self):
        """ Print current commands. """

        table = []
        if self.state == state.IDLE:
            table.extend([
                ["new chatroom", "Host a new chatroom"],
                ["connect", "Connect to a host"],
                ["settings", "Change settings"],
            ])
        if self.state == state.HOSTING or self.state == state.CONNECTED:
            table.append(["disconnect", "Disconnect from the chatroom"])
        if self.state != state.SETTINGS:
            table.append(["exit", "Exit"])
        print_table(table)


    def print_warning(self, msg=None):
        """ Print a warning on the console. """

        # TODO: Print multiple warning messages
        if msg:
            self.warning_msg = msg

        if self.warning_msg:
            print_box(self.warning_msg)

        if msg is None:
            self.warning_msg = None