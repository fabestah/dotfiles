from libqtile.config import Key, KeyChord
from libqtile.lazy import lazy

mod = "mod1" # mod1 = Alt | mod4 = Super
shift = "shift"
terminal = "kitty"
browser = "librewolf"

keys = [
    ### General Shortcuts
    Key([mod, "shift"], "c",
        lazy.window.kill(),
        desc="Kill active window"
        ),
    Key([mod, "control"], "r",
        lazy.restart(),
        desc="Restart Qtile"
        ),
    Key([mod, "control"], "q",
        lazy.shutdown(),
        desc="Shutdown Qtile"
        ),
    ### Spawn Apps
    Key([mod], "r",
        lazy.spawncmd(),
        desc="Spawn a command using a prompt widget"
        ),
    Key([mod], "Return",
        lazy.spawn(terminal),
        desc="Launch my terminal"
        ),
    Key([mod], "b",
        lazy.spawn(browser),
        desc="Launch my browser"
        ),
    Key([mod, "shift"], "Return",
        lazy.spawn("rofi -show drun "),
        desc="Run Rofi"
        ),
    Key([mod, "shift"], "e",
        lazy.spawn("rofi -show emoji"),
        desc="Run Rofi emoji plugin"
        ),
    ### Window Controls
    # Move Focus
    Key([mod], "j",
        lazy.layout.down(),
        desc="Move focus down"
        ),
    Key([mod], "k",
        lazy.layout.up(),
        desc="Move focus up"
        ),
    Key([mod], "space",
        lazy.layout.next(),
        desc='Move focus to next window in current stack'
        ),
    # Adjust Window Size
    Key([mod], "h",
        lazy.layout.shrink(),
        lazy.layout.decrease_nmaster(),
        desc="Shrink window (MonadTall), decrease number in master pane (Tile)"
        ),
    Key([mod], "l",
        lazy.layout.grow(),
        lazy.layout.increase_nmaster(),
        desc="Expand window (MonadTall), increase number in master pane (Tile)"
        ),
    Key([mod], "n",
        lazy.layout.reset(),
        desc="Reset window size ratios"
        ),
    Key([mod], "m",
        lazy.layout.maximize(),
        desc="Toggle window between minimum and maximum sizes"
        ),
    ### Stack Controls
    # Move Windows
    Key([mod, "shift"], "j",
        lazy.layout.shuffle_down(),
        lazy.layout.section_down(),
        desc="Move window down in current stack"
        ), 
    Key([mod, "shift"], "k",
        lazy.layout.shuffle_up(),
        lazy.layout.section_up(),
        desc="Move window up in current stack"
        ),
    Key([mod, "shift"], "Tab",
        lazy.layout.rotate(),
        lazy.layout.flip(),
        desc='Switch which side main pane occupies (MonadTall)'
        ),
    # Toggles
    Key([mod], "Tab",
        lazy.next_layout(),
        desc="Toggle through layouts"
        ),
    Key([mod, "shift"], "f",
        lazy.window.toggle_floating(),
        desc="Toggle floating"
        ),
    Key([mod], "f",
        lazy.window.toggle_fullscreen(),
        desc="Toggle fullscreen"
        ),

    Key([mod, "shift"], "space",
        lazy.layout.toggle_split(),
        desc='Toggle between split and unsplit sides of stack'
        ),
    # Toggle between split and unsplit sides of stack.
    # Split = all windows displayed
    # Unsplit = 1 window displayed, like Max layout, but still with
    # multiple stack panes
]

