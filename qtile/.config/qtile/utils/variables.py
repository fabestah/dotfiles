import json
from utils import dir

directory = f'{dir.get()}/config.json'
variables = {
    'bar': 'decorated',
    'colorscheme': 'catppuccin',
    'terminal': 'kitty',
    'wallpaper_main': '~/Pictures/Wallpapers/floating_astronaut.png',
    'with_battery': False,
    'with_wlan': False,
    'two_monitors': False,
}

try:
    with open(directory, 'r') as file:
        config = json.load(file)
        file.close()
except FileNotFoundError:
    with open(directory, 'w') as file:
        file.write(json.dumps(variables, indent = 2))
        config = variables.copy()
        file.close()
