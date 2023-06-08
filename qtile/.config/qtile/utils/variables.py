import json
from utils import dir


directory = f"{dir.get()}/settings.json"

default_settings = [
    {
        "general": {
            "two_monitors": True,
            "with_wlan": False,
            "with_battery": False,
            "network": "ens33",
        },
        "applications": {
            "terminal": "kitty",
            "editor": "vscodium",
            "browser": "librewolf",
            "mail_client": "thunderbird",
            "note_app": "obsidian",
            "screenshot_app": "flameshot gui",
        },
        "theme": {
            "bar": "decorated",
            "colorscheme": "catppuccin",
            "colors": {
                "color_1": "#DDB6F2",  # mauve
                "color_2": "#F5C2E7",  # pink
                "color_3": "#E8A2AF",  # maroon
                "color_4": "#F28FAD",  # red
                "color_5": "#F8BD96",  # peach
                "color_6": "#FAE3B0",  # yellow
                "color_7": "#ABE9B3",  # green
                "color_8": "#B5E8E0",  # teal
                "color_9": "#96CDFB",  # blue
                "color_10": "#89DCEB",  # sky
                "color_11": "#161320",  # black 0
                "color_12": "#1A1826",  # black 1
                "color_13": "#1E1E2E",  # black 2
                "color_14": "#302D41",  # black 3
                "color_15": "#575268",  # black 4
                "color_16": "#6E6C7E",  # gray 0
                "color_17": "#988BA2",  # gray 1
                "color_18": "#C3BAC6",  # gray 2
                "color_19": "#D9E0EE",  # white
                "color_20": "#C9CBFF",  # lavender
                "color_21": "#F5E0DC",  # rosewater
            },
            "wallpapers": {
                "wallpaper_main": "~/pictures/wallpapers/floating_astronaut.png",
                "wallpaper_sec": "~/pictures/wallpapers/floating_astronaut.png",
            },
            "workspace_names": {
                "workspace_1": "",
                "workspace_2": "",
                "workspace_3": "",
                "workspace_4": "",
                "workspace_5": "",
                "workspace_6": "",
                "workspace_7": "",
                "workspace_8": "",
                "workspace_9": "",
            },
        },
    }
]

try:
    with open(directory, "r") as file:
        settings = json.load(file)
        file.close()
except FileNotFoundError:
    with open(directory, "w") as file:
        file.write(json.dumps(default_settings, indent=2))
        settings = default_settings.copy()
        file.close()


def load_settings(cls):
    def wrap():
        instance = cls()
        with open(directory) as f:
            instance.settings = dict(json.load(f)[0])
            return instance

    return wrap


@load_settings
class Variables:
    def __init__(self):
        pass

    def __getattr__(self, name):
        value = self.settings.get(name)
        if isinstance(value, dict):
            sub_instance = Variables()
            sub_instance.settings = value
            return sub_instance

    def __getitem__(self, name):
        return self.settings[name]

    def __repr__(self):
        return str(self.settings)

    def get(self, key, default=None):
        return self.settings.get(key, default)


var = Variables()

# Catppuccin colors
# "color_1": "#DDB6F2",  # mauve
# "color_2": "#F5C2E7",  # pink
# "color_3": "#E8A2AF",  # maroon
# "color_4": "#F28FAD",  # red
# "color_5": "#F8BD96",  # peach
# "color_6": "#FAE3B0",  # yellow
# "color_7": "#ABE9B3",  # green
# "color_8": "#B5E8E0",  # teal
# "color_9": "#96CDFB",  # blue
# "color_10": "#89DCEB",  # sky
# "color_11": "#161320",  # black 0
# "color_12": "#1A1826",  # black 1
# "color_13": "#1E1E2E",  # black 2
# "color_14": "#302D41",  # black 3
# "color_15": "#575268",  # black 4
# "color_16": "#6E6C7E",  # gray 0
# "color_17": "#988BA2",  # gray 1
# "color_18": "#C3BAC6",  # gray 2
# "color_19": "#D9E0EE",  # white
# "color_20": "#C9CBFF",  # lavender
# "color_21": "#F5E0DC",  # rosewater


# Workspaces with names
# "workspace_1": " WEB",
# "workspace_2": " DEV",
# "workspace_3": " SYS",
# "workspace_4": " DOC",
# "workspace_5": " MAIL",
# "workspace_6": " YT",
# "workspace_7": " MUS",
# "workspace_8": " GAME",
# "workspace_9": " TS",

# Workspaces without names
# "workspace_1": "",
# "workspace_2": "",
# "workspace_3": "",
# "workspace_4": "",
# "workspace_5": "",
# "workspace_6": "",
# "workspace_7": "",
# "workspace_8": "",
# "workspace_9": "",


# Font Awesome icons
#  - code file
#  - directory
#  - game controller
#  - lightning bolt
#  - speech bubble
#  - pen in window
#  - note
#  - pencil
#  - pen
#  - paperclip
#  - discord

# Nerd Font icons
#  - firefox
#  - dev
#  - sys
# ﭮ - discord
#  - spotify
#  - directory
#  - note
