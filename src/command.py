from enum import Enum


class command(Enum):

    NEW_CHATROOM = "new chatroom"
    CONNECT = "connect"
    DISCONNECT = "disconnect"
    SETTINGS = "settings"
    EXIT = "exit"


    def __str__(self):

        return self.lower()


    def lower(self):

        return self.name.lower()