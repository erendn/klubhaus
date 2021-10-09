from enum import Enum


class command(Enum):

    NEW_CONNECTION = "new connection"
    CONNECT = "connect"
    DISCONNECT = "disconnect"
    EXIT = "exit"


    def __str__(self):

        return self.lower()


    def lower(self):

        return self.name.lower()