from src.utils import *
from src.connection import connection


def run():
    """ Run the program. """

    con = None

    while True:
        print_ui()

        command = get_command()

        if command == "new connection":
            con = connection("host", True)
        elif command == "connect":
            con = connection("client")
        elif command == "exit":
            del con
            break


if __name__ == "__main__":
    run()