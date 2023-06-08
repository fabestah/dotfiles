import json

from utils import dir
from utils.variables import var


colorscheme = var.theme.get("colorscheme", "catppuccin.json")

path = f"{dir.get()}/utils/colorscheme/{colorscheme}"


with open(path, "r") as file:
    color = json.load(file)
    file.close()
