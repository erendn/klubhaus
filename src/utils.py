import os
import pyaudio
from .command import command

# Default sound configs
CHUNK = 1024
FORMAT = pyaudio.paInt16
CHANNELS = 2
RATE = 44100


def get_command():
    """ Get a command from the user. """

    com = input()
    for v in command:
        if com == v.value:
            return v


def get_input(msg):
    """ Return a user input. """

    # TODO: Make it fancy looking
    data = input(msg)
    if data.isnumeric():
        data = int(data)
    return data


def print_audio_devices():
    """ Print all audio devices. """

    import pyaudio
    p = pyaudio.PyAudio()
    for i in range(p.get_device_count()):
        dev = p.get_device_info_by_index(i)
        print((i, dev['name'], dev['maxInputChannels']))


def clear_screen():
    """ Clear the terminal/console. """

    os.system("cls" if os.name == "nt" else "clear")


def print_banner():
    """ Print the program banner. """

    print()
    print("  ██╗  ██╗██╗     ██╗   ██╗██████╗ ██╗  ██╗ █████╗ ██╗   ██╗███████╗")
    print("  ██║ ██╔╝██║     ██║   ██║██╔══██╗██║  ██║██╔══██╗██║   ██║██╔════╝")
    print("  █████╔╝ ██║     ██║   ██║██████╔╝███████║███████║██║   ██║███████╗")
    print("  ██╔═██╗ ██║     ██║   ██║██╔══██╗██╔══██║██╔══██║██║   ██║╚════██║")
    print("  ██║  ██╗███████╗╚██████╔╝██████╔╝██║  ██║██║  ██║╚██████╔╝███████║")
    print("  ╚═╝  ╚═╝╚══════╝ ╚═════╝ ╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═╝ ╚═════╝ ╚══════╝")
    print()


def print_table(table, align=None):
    """ Print the given table. """

    if type(table) is dict:
        table = list(map(list, table.items()))

    if len(table) == 0:
        return

    num_rows = len(table)
    num_cols = len(table[0])

    for i in range(num_rows):
        for j in range(num_cols):
            if type(table[i][j]) is not str:
                table[i][j] = str(table[i][j])

    # Calculate the widths of each column
    col_width = []
    for i in range(num_cols):
        col_width.append(0)
        for j in range(num_rows):
            if col_width[-1] < len(str(table[j][i])) + 2:
                col_width[-1] = len(str(table[j][i])) + 2

    print_table_line(col_width, "top")
    for i in range(num_rows):
        for j in range(num_cols):
            if align is None or align[j] == "left":
                text = " " + table[i][j].ljust(col_width[j] - 1)
            elif align[j] == "right":
                text = table[i][j].rjust(col_width[j] - 1) + " "
            elif align[j] == "center":
                text = table[i][j].center(col_width[j])
            print("║" + text, end="")
        print("║")
        if i < num_rows - 1:
            print_table_line(col_width, "middle")
    print_table_line(col_width, "bottom")


def print_table_line(col_width, place):
    """ Print a table row separator line. """

    if place == "top":
        line = "╔"
    elif place == "middle":
        line = "╠"
    elif place == "bottom":
        line = "╚"
    for i in range(len(col_width)):
        line += "═" * col_width[i]
        if place == "top":
            line += "╦"
        elif place == "middle":
            line += "╬"
        elif place == "bottom":
            line += "╩"
    line = line[:-1]
    if place == "top":
        line += "╗"
    elif place == "middle":
        line += "╣"
    elif place == "bottom":
        line += "╝"
    print(line)


def print_box(msg, align="left"):
    """ Print a box of text. """

    lines = msg.splitlines()
    max_width = 0
    for line in lines:
        if len(line) + 2 > max_width:
            max_width = len(line) + 2

    print_table_line([max_width], "top")
    for line in lines:
        if align == "left":
            text = " " + line.ljust(max_width - 1)
        elif align == "right":
            text = line.rjust(max_width - 1) + " "
        elif align == "center":
            text = line.center(max_width)
        print("║" + text + "║")
    print_table_line([max_width], "bottom")