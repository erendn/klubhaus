import os
import keyboard
import pyaudio

# Program variables
CON = None
STATE = None

# Default socket configs
HOST = "localhost"
PORT = 5000
BACKLOG = 5

# Default sound configs
CHUNK = 1024
FORMAT = pyaudio.paInt16
CHANNELS = 2
RATE = 44100

WARNING_MSG = None


def get_command():
    """ Get a command from the user. """

    key = keyboard.read_key()

    if key == "n":
        return "new connection"
    elif key == "c":
        return "connect"
    elif key == "esc":
        return "exit"


def get_input(msg):
    """ Return a user input. """

    # TODO: Make it fancy looking
    data = input(msg)
    if data.isnumeric():
        data = int(data)
    return data


def print_ui():
    """ Print the console UI of the program. """

    clear_screen()
    print_banner()
    print_commands()
    print_warning()


def clear_screen():
    """ Clear the terminal/console. """

    os.system('cls' if os.name=='nt' else 'clear')


def print_banner():
    """ Print the program banner. """

    print()
    print("   ██████╗██╗  ██╗ █████╗ ████████╗████████╗███████╗██████╗   ")
    print("  ██╔════╝██║  ██║██╔══██╗╚══██╔══╝╚══██╔══╝██╔════╝██╔══██╗  ")
    print("  ██║     ███████║███████║   ██║      ██║   █████╗  ██████╔╝  ")
    print("  ██║     ██╔══██║██╔══██║   ██║      ██║   ██╔══╝  ██╔══██╗  ")
    print("  ╚██████╗██║  ██║██║  ██║   ██║      ██║   ███████╗██║  ██║  ")
    print("   ╚═════╝╚═╝  ╚═╝╚═╝  ╚═╝   ╚═╝      ╚═╝   ╚══════╝╚═╝  ╚═╝  ")
    print()


def print_commands():
    """ Print current commands. """

    print()
    print("Press N to host a new connection")
    print("Press C to connect to a host")
    print("Press Esc to exit")
    print()


def print_warning(msg=None):
    """ Print a warning on the console. """
    global WARNING_MSG

    if msg:
        WARNING_MSG = msg

    if WARNING_MSG:
        print()
        print("╔" + "═" * (len(WARNING_MSG) + 4) + "╗")
        print("║  " + WARNING_MSG + "  ║")
        print("╚" + "═" * (len(WARNING_MSG) + 4) + "╝")
        print()

    if msg is None:
        WARNING_MSG = None