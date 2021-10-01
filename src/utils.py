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


def print_banner():
    print()
    print("   ██████╗██╗  ██╗ █████╗ ████████╗████████╗███████╗██████╗   ")
    print("  ██╔════╝██║  ██║██╔══██╗╚══██╔══╝╚══██╔══╝██╔════╝██╔══██╗  ")
    print("  ██║     ███████║███████║   ██║      ██║   █████╗  ██████╔╝  ")
    print("  ██║     ██╔══██║██╔══██║   ██║      ██║   ██╔══╝  ██╔══██╗  ")
    print("  ╚██████╗██║  ██║██║  ██║   ██║      ██║   ███████╗██║  ██║  ")
    print("   ╚═════╝╚═╝  ╚═╝╚═╝  ╚═╝   ╚═╝      ╚═╝   ╚══════╝╚═╝  ╚═╝  ")
    print()