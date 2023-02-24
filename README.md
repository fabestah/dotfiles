# dotfiles

## Usage

- ### Integrate dotfiles in your $HOME
  1. Clone the repo `git clone https://github.com/fabestah/dotfiles.git`
  2. Cd into the cloned dotfiles directory
  3. Stow one or more packages: `stow -vSt ~ zsh qtile`
(always simulate your operation before actually invoking it with `stow -nvSt`)

- ### Install Packages from my Packages List
  - Install all packages (with an AUR helper): `yay -S < packages.list`
  - Only install pacman packages: `sudo pacman -S $(comm -12 <(pacman -Slq | sort) <(sort packages.list))`
  - Uninstall packages not listed in the packages list: `sudo pacman -Rsu $(comm -23 <(pacman -Qq | sort) <(sort packages.list))`
