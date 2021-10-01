from src.utils import *
from src.connection import connection


def new_connection():
    """ Host a new connection. """
    global CON

    if CON:
        print_warning("You can only host 1 connection at the same time.")
    else:
        port = get_input("Enter the port number: ")
        CON = connection(username="host",
                         port=port,
                         is_host=True)


def connect():
    """ Connect to a host. """
    global CON

    if CON:
        print_warning("You can only connect to 1 host at the same time.")
    else:
        port = get_input("Enter the port number: ")
        CON = connection(username="client",
                         port=port)


def exit():
    """ Exit the program. """
    global CON

    del CON


def run():
    """ Run the program. """

    while True:
        print_ui()

        command = get_command()

        if command == "new connection":
            new_connection()
        elif command == "connect":
            connect()
        elif command == "exit":
            exit()
            break


if __name__ == "__main__":
    run()