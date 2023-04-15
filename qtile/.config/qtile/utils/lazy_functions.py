from libqtile import qtile
from libqtile.backend.base import Window
from libqtile.config import Screen
from libqtile.core.manager import Qtile
from libqtile.lazy import lazy


def move_window_to_screen(qtile: Qtile, window: Window, screen: Screen):
    """Moves a window to a screen and focuses it, allowing you to move it
    further if you wish."""
    window.togroup(screen.group.name)
    qtile.focus_screen(screen.index)
    screen.group.focus(window, True)


qtile: Qtile = qtile


@lazy.function
def move_window_to_next_screen(_):
    """Moves a window to the next screen. Loops around the beginning and
    end."""
    index = qtile.current_screen.index
    index = index + 1 if index < len(qtile.screens) - 1 else 0
    move_window_to_screen(qtile, qtile.current_window, qtile.screens[index])


@lazy.function
def move_window_to_prev_screen(_):
    """Moves a window to the previous screen. Loops around the beginning and
    end."""
    index = qtile.current_screen.index
    index = index - 1 if index > 0 else len(qtile.screens) - 1
    move_window_to_screen(qtile, qtile.current_window, qtile.screens[index])


@lazy.function
def move_focus_to_next_screen(_):
    """Moves the focus to the next screen. Loops around the beginning and
    end."""
    index = qtile.current_screen.index
    index = index + 1 if index < len(qtile.screens) - 1 else 0
    qtile.focus_screen(qtile.screens[index].index)


@lazy.function
def move_focus_to_prev_screen(_):
    """Moves the focus to the previous screen. Loops around the beginning and
    end."""
    index = qtile.current_screen.index
    index = index - 1 if index > 0 else len(qtile.screens) - 1
    qtile.focus_screen(qtile.screens[index].index)


@lazy.function
def minimize_all_windows(qtile):
    """Minimizes all windows in focused group."""
    for win in qtile.current_group.windows:
        if hasattr(win, "toggle_minimize"):
            win.toggle_minimize()
