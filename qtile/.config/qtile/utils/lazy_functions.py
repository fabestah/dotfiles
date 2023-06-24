from libqtile import qtile
from libqtile.backend.base import Window
from libqtile.config import Screen
from libqtile.core.manager import Qtile
from libqtile.lazy import lazy


class Functions:
    qtile: Qtile = qtile

    @staticmethod
    def move_window_to_screen(qtile: Qtile, window: Window, screen: Screen):
        """Moves a window to a screen and focuses it, allowing you to move it
        further if you wish."""
        window.togroup(screen.group.name)
        qtile.focus_screen(screen.index)
        screen.group.focus(window, True)

    @staticmethod
    @lazy.function
    def move_window_to_next_screen(_):
        """Moves a window to the next screen. Loops around the beginning and
        end."""
        index = Functions.qtile.current_screen.index
        index = index + 1 if index < len(Functions.qtile.screens) - 1 else 0
        Functions.move_window_to_screen(
            Functions.qtile,
            Functions.qtile.current_window,
            Functions.qtile.screens[index],
        )

    @staticmethod
    @lazy.function
    def move_window_to_prev_screen(_):
        """Moves a window to the previous screen. Loops around the beginning and
        end."""
        index = Functions.qtile.current_screen.index
        index = index - 1 if index > 0 else len(Functions.qtile.screens) - 1
        Functions.move_window_to_screen(
            Functions.qtile,
            Functions.qtile.current_window,
            Functions.qtile.screens[index],
        )

    @staticmethod
    @lazy.function
    def move_focus_to_next_screen(_):
        """Moves the focus to the next screen. Loops around the beginning and
        end."""
        index = Functions.qtile.current_screen.index
        index = index + 1 if index < len(Functions.qtile.screens) - 1 else 0
        Functions.qtile.focus_screen(Functions.qtile.screens[index].index)

    @staticmethod
    @lazy.function
    def move_focus_to_prev_screen(_):
        """Moves the focus to the previous screen. Loops around the beginning and
        end."""
        index = Functions.qtile.current_screen.index
        index = index - 1 if index > 0 else len(Functions.qtile.screens) - 1
        Functions.qtile.focus_screen(Functions.qtile.screens[index].index)

    @staticmethod
    @lazy.function
    def minimize_all_windows(_):
        """Minimizes all windows in focused group."""
        for win in Functions.qtile.current_group.windows:
            if hasattr(win, "toggle_minimize"):
                win.toggle_minimize()
