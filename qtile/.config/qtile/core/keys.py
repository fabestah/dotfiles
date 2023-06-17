from libqtile.config import Key, KeyChord
from libqtile.lazy import lazy

from utils import var
from utils.lazy_functions import (
    move_window_to_next_screen,
    move_window_to_prev_screen,
    move_focus_to_next_screen,
    move_focus_to_prev_screen,
    minimize_all_windows,
)


mod = var.general["mod"]  # mod1 = Alt | mod4 = Super


keys = [
    ### General
    Key([mod, "shift"], "c", lazy.window.kill(), desc="Kill active window"),
    Key([mod, "control"], "r", lazy.restart(), desc="Restart Qtile"),
    Key([mod, "control"], "q", lazy.shutdown(), desc="Shutdown Qtile"),
    ### Move focus
    Key([mod], "j", lazy.layout.down(), desc="Move focus down"),
    Key([mod], "k", lazy.layout.up(), desc="Move focus up"),
    Key(
        [mod],
        "space",
        lazy.layout.next(),
        desc="Move focus to next window in current stack",
    ),
    # Key([mod], r_shift,
    #    lazy.next_screen(),
    #    desc='Move focus to next monitor'
    #   ),
    Key(
        [mod],
        "comma",
        move_focus_to_next_screen,
        desc="Move focus to next screen",
    ),
    Key(
        [mod],
        "period",
        move_focus_to_prev_screen,
        desc="Move focus to previous screen",
    ),
    ### Adjust window size
    Key(
        [mod, "shift"],
        "h",
        lazy.layout.shrink(),
        lazy.layout.decrease_nmaster(),
        desc="Shrink window (MonadTall), decrease number in master pane (Tile)",
    ),
    Key(
        [mod, "shift"],
        "l",
        lazy.layout.grow(),
        lazy.layout.increase_nmaster(),
        desc="Expand window (MonadTall), increase number in master pane (Tile)",
    ),
    Key(
        [mod, "shift"],
        "r",
        lazy.layout.reset(),
        desc="Reset window size ratios",
    ),
    Key(
        [mod, "shift"],
        "m",
        lazy.layout.maximize(),
        desc="Toggle window between minimum and maximum sizes",
    ),
    ### Move windows
    Key(
        [mod, "shift"],
        "j",
        lazy.layout.shuffle_down(),
        lazy.layout.section_down(),
        desc="Move window down in current stack",
    ),
    Key(
        [mod, "shift"],
        "k",
        lazy.layout.shuffle_up(),
        lazy.layout.section_up(),
        desc="Move window up in current stack",
    ),
    Key(
        [mod, "shift"],
        "Tab",
        lazy.layout.rotate(),
        lazy.layout.flip(),
        desc="Switch which side main pane occupies (MonadTall)",
    ),
    Key(
        [mod, "shift"],
        "comma",
        move_window_to_next_screen,
        desc="Move window to next screen",
    ),
    Key(
        [mod, "shift"],
        "period",
        move_window_to_prev_screen,
        desc="Move window to previous screen",
    ),
    Key(
        [mod, "shift"],
        "minus",
        minimize_all_windows,
        desc="Minimize all windows in focused group",
    ),
    ### Toggles
    Key(
        [mod], "Tab", lazy.next_layout(), desc="Toggle through layouts forward"
    ),
    Key(
        [mod, "shift"],
        "Tab",
        lazy.prev_layout(),
        desc="Toggle through layouts backwards",
    ),
    Key(
        [mod, "shift"],
        "f",
        lazy.window.toggle_floating(),
        desc="Toggle floating",
    ),
    Key([mod], "f", lazy.window.toggle_fullscreen(), desc="Toggle fullscreen"),
    Key(
        [mod, "shift"],
        "space",
        lazy.layout.toggle_split(),
        desc="Toggle between split and unsplit sides of stack",
    ),
    # Split = all windows displayed
    # Unsplit = 1 window displayed, like Max layout, but still with multiple stack panes
    Key(
        [mod],
        "m",
        lazy.window.toggle_maximize(),
        desc="Toggle window between minimum and maximum size",
    ),
    ### Media keys
    Key(
        [],
        "XF86AudioMute",
        lazy.spawn("amixer -D pulse sset Master toggle"),
        desc="Mute/unmute sound volume",
    ),
    Key(
        [],
        "XF86AudioLowerVolume",
        lazy.spawn("amixer -D pulse sset Master 1%-"),
        desc="Lower sound volume",
    ),
    Key(
        [],
        "XF86AudioRaiseVolume",
        lazy.spawn("amixer -D pulse sset Master 1%+"),
        desc="Raise sound volume",
    ),
    Key(
        [],
        "XF86AudioPlay",
        lazy.spawn("playerctl play-pause"),
        desc="Play/pause player",
    ),
    Key(
        [],
        "XF86AudioNext",
        lazy.spawn("playerctl next"),
        desc="Skip to next",
    ),
    Key(
        [],
        "XF86AudioPrev",
        lazy.spawn("playerctl previous"),
        desc="Skip to previous",
    ),
    ### Programs
    Key(
        [mod],
        "s",
        lazy.spawncmd(),
        desc="Spawn a command using a prompt widget",
    ),
    Key(
        [mod],
        "Return",
        lazy.spawn(var.applications["terminal"]),
        desc="Launch a terminal",
    ),
    Key(
        [mod],
        "b",
        lazy.spawn(var.applications["browser"]),
        desc="Launch browser",
    ),
    Key(
        [mod, "shift"],
        "Return",
        lazy.spawn(var.applications["app_launcher"]),
        desc="Lunch application launcher",
    ),
    Key(
        [mod],
        "m",
        lazy.spawn(var.applications["mail_client"]),
        desc="Launch mail client",
    ),
    Key(
        [mod],
        "c",
        lazy.spawn(var.applications["editor"]),
        desc="Launch code editor",
    ),
    Key(
        [mod],
        "o",
        lazy.spawn(var.applications["note_app"]),
        desc="Launch note taking application",
    ),
    Key(
        ["control", "shift"],
        "s",
        lazy.spawn(var.applications["screenshot_app"]),
        desc="Launch screenshot tool",
    ),
    Key(
        [mod],
        "e",
        lazy.spawn("emoji-picker"),
        desc="Launch emoji picking tool",
    ),
    Key(
        [mod],
        "t",
        lazy.group["scratchpad"].dropdown_toggle("term"),
        desc="Toggle drop-down terminal",
    ),
    Key(
        [mod, "shift"],
        "t",
        lazy.group["scratchpad"].dropdown_toggle("btop-term"),
        desc="Toggle drop-down btop ressource monitor",
    ),
    Key(
        [mod, "shift"],
        "p",
        lazy.spawn("rofi -show window"),
        desc="Launch window switcher",
    ),
    Key(
        [mod, "control"],
        "c",
        lazy.spawn("rofi -show calc -no-show-match -no-sort"),
        desc="Launch window switcher",
    ),
    # To-Do: Screenshots, Audio, Brightness, Misc, KeyChords
]
