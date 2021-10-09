from enum import Enum, auto


class command(Enum):

    NEW_CONNECTION = auto()
    CONNECT = auto()
    DISCONNECT = auto()
    EXIT = auto()


    def __str__(self):

        return self.lower()


    def lower(self):

        return self.name.lower()