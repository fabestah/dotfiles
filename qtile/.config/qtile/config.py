from libqtile import bar, layout, widget
from libqtile.config import Click, Drag, Group, Key, Match, Screen
from libqtile.lazy import lazy

from core import (
        groups,
        keys,
        mod,
        shift,

)

from libqtile.dgroups import simple_key_binder

TERMINAL = "kitty"
BROWSER = "librewolf"
FONT_MAIN = "ttf-hack-nerd"


#  LAYOUTS 

LAYOUT_THEME_MAIN = {"border_width": 1,
                "margin": 14,
                "border_focus": "e1acff",
                "border_normal": "1D2330"
                }

layouts = [
    # layout.MonadWide(**layout_theme),
    # layout.Bsp(**layout_theme),
    # layout.Stack(stacks=2, **layout_theme),
    # layout.Columns(**layout_theme),
    # layout.RatioTile(**layout_theme),
    # layout.Tile(shift_windows=True, **layout_theme),
    # layout.VerticalTile(**layout_theme),
    # layout.Matrix(**layout_theme),
    # layout.Zoomy(**layout_theme),
    # layout.Max(**layout_theme),
    layout.MonadTall(**LAYOUT_THEME_MAIN),
    layout.MonadWide(**LAYOUT_THEME_MAIN),
    layout.Stack(num_stacks=2),
    layout.TreeTab(
         font = "Ubuntu",
         fontsize = 10,
         sections = ["FIRST", "SECOND", "THIRD", "FOURTH"],
         section_fontsize = 10,
         border_width = 2,
         bg_color = "1c1f24",
         active_bg = "c678dd",
         active_fg = "000000",
         inactive_bg = "a9a1e1",
         inactive_fg = "1c1f24",
         padding_left = 0,
         padding_x = 0,
         padding_y = 5,
         section_top = 10,
         section_bottom = 20,
         level_shift = 8,
         vspace = 3,
         panel_width = 200
         ),
    layout.Floating(**LAYOUT_THEME_MAIN)
]


#  WIDGETS 

# Default Widget Settings
widget_defaults = dict(
    font="ttf-hack-nerd",
    fontsize=14,
    padding=3
    # background = colors[2]
)
extension_defaults = widget_defaults.copy()

def init_widgets_list():
    widgets_list = [
            # Margin
            widget.Spacer(
                length = 12,
                #foreground = colors[2],
                #background = color[0]
                ),
            widget.CurrentLayout(),
            widget.GroupBox(),
            widget.Prompt(),
            widget.WindowName(),
            widget.Chord(
                chords_colors={
                    "launch": ("#ff0000", "#ffffff"),
                },
                name_transform=lambda name: name.upper(),
            ),
            widget.CheckUpdates(
                distro = "Arch",
                display_format = "Updates: {updates}"
                ),
            widget.Systray(),
            #widget.CurrentLayoutIcon(
            #    custom_icon_paths = ["/home/fabestah/.config/qtile/icons"]
            #    foreground = colors[2],
            #    background = colors[0],
            #    padding = 0
            #    scale = 0.7
            #    ),
            widget.CPU(
                format = "{load_percent}%",
                update_interval = 0.5
                ),
            widget.CheckUpdates(
                update_interval = 1800,
                distro = 'Arch_checkupdates',
                display_format = 'Updates: {updates}',
                mouse_callbacks = {"Button1": lambda: qtile.cmd_spawn(TERMINAL + ' -e sudo pacman -Syu')},
                font = FONT_MAIN,
                foreground = "ffffff",
                #background = color[0],
                colour_have_updates = "ffffff",
                colour_no_updates = "ffffff",
                padding = 5,
                #decorations = [
                #    BorderDecoration(
                #        #colour = colors[5],
                #        border_width = [0, 0, 2, 0],
                #        padding_x = 5,
                #        padding_y = None,
                #    )
                #],
                ),
            widget.Clock(format="%Y-%m-%d %a %I:%M %p"),
            widget.QuickExit(),
            ]
    return widgets_list

def init_widgets_screen1():
    widgets_screen1 = init_widgets_list()
    return widgets_screen1

def init_screens():
    return [Screen(top=bar.Bar(widgets=init_widgets_screen1(), opacity=1.0, size=20))]

if __name__ in ["config", "__main__"]:
    screens = init_screens()
    #widgets_list = init_widgets_list()
    widgets_screen1 = init_widgets_screen1()


dgroups_key_binder = None
dgroups_app_rules = []  # type: list
follow_mouse_focus = True
bring_front_click = False
cursor_warp = False
floating_layout = layout.Floating(
    float_rules=[
        # Run the utility of `xprop` to see the wm class and name of an X client.
        *layout.Floating.default_float_rules,
        Match(wm_class="confirmreset"),  # gitk
        Match(wm_class="makebranch"),  # gitk
        Match(wm_class="maketag"),  # gitk
        Match(wm_class="ssh-askpass"),  # ssh-askpass
        Match(title="branchdialog"),  # gitk
        Match(title="pinentry"),  # GPG key password entry
    ]
)
auto_fullscreen = True
focus_on_window_activation = "smart"
reconfigure_screens = True

# If things like steam games want to auto-minimize themselves when losing
# focus, should we respect this or not?
auto_minimize = True

# When using the Wayland backend, this can be used to configure input devices.
wl_input_rules = None

# XXX: Gasp! We're lying here. In fact, nobody really uses or cares about this
# string besides java UI toolkits; you can see several discussions on the
# mailing lists, GitHub issues, and other WM documentation that suggest setting
# this string if your java app doesn't work correctly. We may as well just lie
# and say that we're a working one by default.
#
# We choose LG3D to maximize irony: it is a 3D non-reparenting WM written in
# java that happens to be on java's whitelist.
wmname = "LG3D"
