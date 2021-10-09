from enum import Enum, auto


class state(Enum):

    IDLE = auto()
    CONNECTED = auto()
    HOSTING = auto()