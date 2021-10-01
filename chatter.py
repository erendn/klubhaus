import sys
from src.utils import *
from src.connection import connection


if __name__ == "__main__":
    print_banner()

    if sys.argv[1] == "host":
        con = connection("host", True)
    elif sys.argv[1] == "client":
        con = connection("client")

    if input() == "exit":
        del con