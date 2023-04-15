from libqtile import layout
from libqtile.config import Match

from utils import color

layout_theme = {
    "border_width": 2,
    "margin": 14,
    "border_focus": color["fg"],
    "border_normal": color["bg"],
    "font": "Hack Nerd Font",
    "grow_amount": 1,
}

layouts = [
    layout.MonadTall(**layout_theme, ratio=0.6),
    layout.MonadWide(**layout_theme),
    layout.Stack(num_stacks=2),
    layout.Floating(**layout_theme),
    layout.TreeTab(
        fontsize=10,
        sections=["FIRST", "SECOND", "THIRD", "FOURTH"],
        section_fontsize=10,
        border_width=2,
        bg_color="1c1f24",
        active_bg="c678dd",
        active_fg="000000",
        inactive_bg="a9a1e1",
        inactive_fg="1c1f24",
        padding_left=0,
        padding_x=0,
        padding_y=5,
        section_top=10,
        section_bottom=20,
        level_shift=8,
        vspace=3,
        panel_width=200,
    ),
]

floating_layout = layout.Floating(
    **layout_theme,
    float_rules=[
        # Run the utility of `xprop` to see the wm class and name of an X client.
        *layout.Floating.default_float_rules,
        Match(wm_class="confirmreset"),  # gitk
        Match(wm_class="makebranch"),  # gitk
        Match(wm_class="maketag"),  # gitk
        Match(wm_class="ssh-askpass"),  # ssh-askpass
        Match(title="branchdialog"),  # gitk
        Match(title="pinentry"),  # GPG key password entry
        Match(title="veracrypt"),
        # TODO add matches
    ],
)
