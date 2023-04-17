import json

from utils import dir
from utils.variables import settings

colorscheme = {"catppuccin": "catppuccin.json"}.get(
    settings["colorscheme"], "catppuccin.json"
)

path = f"{dir.get()}/utils/colorscheme/{colorscheme}"

with open(path, "r") as file:
    color = json.load(file)
    file.close()
