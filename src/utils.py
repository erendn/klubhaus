import os
import keyboard


def get_command():
    """ Get a command from the user. """

    key = keyboard.read_key()

    if key == "n":
        return "new connection"
    elif key == "c":
        return "connect"
    elif key == "d":
        return "disconnect"
    elif key == "esc":
        return "exit"


def get_input( msg):
    """ Return a user input. """

    # TODO: Make it fancy looking
    data = input(msg)
    if data.isnumeric():
        data = int(data)
    return data


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