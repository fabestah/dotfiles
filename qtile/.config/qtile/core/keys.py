from libqtile.config import Key, KeyChord
from libqtile.lazy import lazy

from utils.lazy_functions import (
    move_window_to_next_screen,
    move_window_to_prev_screen,
    move_focus_to_next_screen,
    move_focus_to_prev_screen,
    minimize_all_windows,
)


mod = "mod1"  # mod1 = Alt | mod4 = Super
shift = "shift"
ctrl = "control"

terminal = "kitty"
browser = "librewolf"
mail_client = "thunderbird"
code_editor = "codium"
note_app = "obsidian"
crypto_app = "veracrypt"
screenshot_app = "flameshot gui"
emoji_app = "emoji-keyboard"


keys = [
    ### General
    Key([mod, shift], "c", lazy.window.kill(), desc="Kill active window"),
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
        [mod, shift],
        "h",
        lazy.layout.shrink(),
        lazy.layout.decrease_nmaster(),
        desc="Shrink window (MonadTall), decrease number in master pane (Tile)",
    ),
    Key(
        [mod, shift],
        "l",
        lazy.layout.grow(),
        lazy.layout.increase_nmaster(),
        desc="Expand window (MonadTall), increase number in master pane (Tile)",
    ),
    Key(
        [mod, shift], "r", lazy.layout.reset(), desc="Reset window size ratios"
    ),
    Key(
        [mod, shift],
        "m",
        lazy.layout.maximize(),
        desc="Toggle window between minimum and maximum sizes",
    ),
    ### Move windows
    Key(
        [mod, shift],
        "j",
        lazy.layout.shuffle_down(),
        lazy.layout.section_down(),
        desc="Move window down in current stack",
    ),
    Key(
        [mod, shift],
        "k",
        lazy.layout.shuffle_up(),
        lazy.layout.section_up(),
        desc="Move window up in current stack",
    ),
    Key(
        [mod, shift],
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
        [mod, shift],
        "Tab",
        lazy.prev_layout(),
        desc="Toggle through layouts backwards",
    ),
    Key(
        [mod, shift],
        "f",
        lazy.window.toggle_floating(),
        desc="Toggle floating",
    ),
    Key([mod], "f", lazy.window.toggle_fullscreen(), desc="Toggle fullscreen"),
    Key(
        [mod, shift],
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
    ### Programs
    Key(
        [mod],
        "s",
        lazy.spawncmd(),
        desc="Spawn a command using a prompt widget",
    ),
    Key([mod], "Return", lazy.spawn(terminal), desc="Launch terminal"),
    Key([mod], "b", lazy.spawn(browser), desc="Launch browser"),
    Key([mod], "m", lazy.spawn(mail_client), desc="Launch mail client"),
    Key([mod], "c", lazy.spawn(code_editor), desc="Launch VSCodium"),
    Key([mod], "o", lazy.spawn(note_app), desc="Launch Obsidian"),
    Key([mod], "v", lazy.spawn(crypto_app), desc="Launch VeraCrypt"),
    Key([mod], "e", lazy.spawn(emoji_app), desc="Launch Emoji keyboard"),
    Key(
        [ctrl, shift], "s", lazy.spawn(screenshot_app), desc="Launch flameshot"
    ),
    Key(
        [mod, shift], "Return", lazy.spawn("rofi -show drun "), desc="Run Rofi"
    ),
    Key(
        [mod, shift],
        "e",
        lazy.spawn("rofi -show emoji"),
        desc="Run Rofi emoji plugin",
    ),
    Key(
        [mod],
        "t",
        lazy.group["scratchpad"].dropdown_toggle("term"),
        desc="Toggle drop-down Kitty terminal",
    ),
    Key(
        [mod, shift],
        "t",
        lazy.group["scratchpad"].dropdown_toggle("btop-term"),
        desc="Toggle drop-down btop ressource monitor",
    ),
    # To-Do: Screenshots, Audio, Brightness, Misc, KeyChords
]
