from json import loads, dumps

# This dict object stores all settings of the app
SETTINGS = None


def change_setting(key, value):
    """ Change a setting. """
    global SETTINGS

    SETTINGS[key] = value
    save_settings()


def save_settings():
    """"""
    global SETTINGS

    with open("settings.json", "w") as file:
        file.write(dumps(SETTINGS, indent=4))


def load_settings():
    """"""
    global SETTINGS

    with open("settings.json", "r") as file:
        SETTINGS = loads(file.read())


# Load settings while importing this module
load_settings()