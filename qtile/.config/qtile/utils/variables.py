import json
from utils import dir
from typing import Any, Callable, TypeVar
from libqtile.log_utils import logger


T = TypeVar("T", bound="Variables")

directory: str = f"{dir.get()}/settings.json"

default_settings: dict[str, Any] = {
    "general": {
        "mod": "mod1",
        "network": "ens33",
        "two_monitors": True,
        "with_battery": False,
        "with_wlan": False,
    },
    "applications": {
        "terminal": "kitty",
        "editor": "vscodium",
        "browser": "librewolf",
        "app_launcher": "rofi -show drun",
        "mail_client": "thunderbird",
        "note_app": "obsidian",
        "screenshot_app": "flameshot gui",
    },
    "theme": {
        "bar": "decorated",
        "colorscheme": "catppuccin.json",
        "wallpapers": {
            "wallpaper_main": "~/pictures/wallpapers/floating_astronaut.png",
            "wallpaper_sec": "~/pictures/wallpapers/floating_astronaut.png",
        },
        "workspace_names": {
            "workspace_0": "\ue007",
            "workspace_1": "\uf121",
            "workspace_2": "\uf120",
            "workspace_3": "\uf70e",
            "workspace_4": "\uf0e0",
            "workspace_5": "\uf167",
            "workspace_6": "\uf1bc",
            "workspace_7": "\uf412",
            "workspace_8": "\uf4f9",
        },
    },
}


def load_settings(cls: type[T]) -> Callable[[], T]:
    def wrap() -> T:
        instance: T = cls()
        instance.settings = read_settings_file()
        return instance

    def read_settings_file() -> dict[str, Any]:
        try:
            with open(directory) as f:
                return dict(json.load(f))
        except json.JSONDecodeError as e:
            logger.exception(e)
            return default_settings
        except FileNotFoundError as e:
            logger.exception(e)
            return create_default_settings_file()

    def create_default_settings_file() -> dict[str, Any]:
        with open(directory, "w") as f:
            json.dump(default_settings, f, indent=4)
        return default_settings

    return wrap


@load_settings
class Variables:
    def __init__(self):
        self.settings: dict[str, Any]

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

    def get_workspace_names_list(self) -> list[str]:
        workspace_names = self.theme.get("workspace_names").values()
        return list(workspace_names)


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
