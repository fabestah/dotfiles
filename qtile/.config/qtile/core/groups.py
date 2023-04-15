from libqtile.config import Group, Key, Match, ScratchPad, DropDown
from libqtile.lazy import lazy

from core.keys import keys, mod, shift
from utils.settings import workspace_names


workspaces = [
    {
        "name": workspace_names[0],
        "key": "1",
        "matches": [Match(wm_class="firefox"), Match(wm_class="librewolf")],
        "lay": "monadtall",
        "init": True,
    },
    {
        "name": workspace_names[1],
        "key": "2",
        "matches": [Match(wm_class="code-oss")],
        "lay": "monadtall",
    },
    {"name": workspace_names[2], "key": "3", "lay": "monadtall"},
    {
        "name": workspace_names[3],
        "key": "4",
        "matches": [Match(wm_class="discord")],
        "lay": "monadtall",
    },
    {
        "name": workspace_names[4],
        "key": "5",
        "matches": [Match(wm_class="Spotify")],
        "lay": "monadtall",
        "init": True,
    },
    {"name": workspace_names[5], "key": "6", "lay": "monadtall"},
    {
        "name": workspace_names[6],
        "key": "7",
        "matches": [Match(wm_class="cypress")],
        "lay": "monadtall",
    },
    {"name": workspace_names[7], "key": "8", "lay": "monadtall"},
    {"name": workspace_names[8], "key": "9", "lay": "monadtall"},
]


# workspaces = [
#    {"name": workspace_names[0], "key": "1", "matches": [Match(wm_class="firefox")], "lay": "monadtall"},
#    {"name": workspace_names[1], "key": "2", "matches": [Match(wm_class="code-oss")], "lay": "monadtall"},
#    {"name": workspace_names[2], "key": "3", "matches": [], "lay": "monadtall"},
#    {"name": workspace_names[3], "key": "4", "matches": [Match(wm_class="discord")], "lay": "monadtall"},
#    {"name": workspace_names[4], "key": "5", "matches": [Match(wm_class="Spotify")], "lay": "monadtall"},
#    {"name": workspace_names[5], "key": "6", "matches": [], "lay": "monadtall"},
#    {"name": workspace_names[6], "key": "7", "matches": [Match(wm_class="cypress")], "lay": "monadtall"},
# ]


groups = [Group(i) for i in "123456789"]


# New feature test

# groups = [Group(i) for i in "123456789"]

# for i, workspace in enumerate(workspaces, start=1):
#    matches = workspace["matches"] if "matches" in workspace else None
#    init = workspace["init"] if "init" in workspace else False
#    groups.append(Group(f"{i}", matches=matches, layout=workspace["lay"], init=init, label=workspace["name"]))
#    keys.append(
#        Key(
#            [mod],
#            f"{i}",
#            lazy.group[f"{i}"].toscreen(toggle=True),
#            desc="Focus this workspace",
#        )
#    )
#    keys.append(
#        Key(
#            [mod, shift],
#            f"{i}",
#            *(
#                lazy.window.togroup(f"{i}"),
#                lazy.group[f"{i}"].toscreen(toggle=True),
#            ),
#            desc="Move focused window to another workspace",
#        )
#    )


for workspace in workspaces:
    # matches = workspace["matches"] if "matches" in workspace else None
    # init = workspace["init"] if "init" in workspace else False
    matches = workspace["matches"] if "matches" in workspace else None
    groups.append(
        Group(workspace["name"], matches=matches, layout=workspace["lay"])
    )
    keys.append(
        Key(
            [mod],
            workspace["key"],
            lazy.group[workspace["name"]].toscreen(toggle=True),
            desc="Focus this workspace",
        )
    )
    keys.append(
        Key(
            [mod, shift],
            workspace["key"],
            *(
                lazy.window.togroup(workspace["name"]),
                lazy.group[workspace["name"]].toscreen(toggle=True),
            ),
            desc="Move focused window to another workspace",
        )
    )


# Drop-down Programs:
groups.append(
    ScratchPad(
        "scratchpad",
        [
            DropDown(
                "term",
                "kitty",
                opacity=1,
                x=0.1,
                y=0.08,
                width=0.8,
                height=0.85,
                on_focus_lost_hide=True,
            ),
            DropDown(
                "btop-term",
                "kitty btop",
                opacity=1,
                x=0.1,
                y=0.15,
                width=0.8,
                height=0.7,
                on_focus_lost_hide=True,
            ),
        ],
    )
)
