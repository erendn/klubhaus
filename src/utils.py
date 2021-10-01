import os
import keyboard
import pyaudio

# Default socket configs
HOST = "localhost"
PORT = 5000
BACKLOG = 5

# Default sound configs
CHUNK = 1024
FORMAT = pyaudio.paInt16
CHANNELS = 2
RATE = 44100


def get_command():
    """ Get a command from the user. """

    key = keyboard.read_key()

    if key == "n":
        return "new connection"
    elif key == "c":
        return "connect"
    elif key == "esc":
        return "exit"


def print_ui():
    """ Print the console UI of the program. """

    clear_screen()
    print_banner()
    print_commands()


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
    print("Press N for new connections")
    print("Press Esc to exit")
    print()