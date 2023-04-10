# dotfiles

## Usage

- ### Stowing my dotfiles to your $HOME
  In order to stow my dotfiles you must have `git` and GNU `stow` installed.
  
  1. Clone my repo (no specific location required) and `cd` into the cloned dotfiles directory.
  ```shell
  git clone https://github.com/fabestah/dotfiles.git
  ```
  2. Simulate your `stow` operation before actually invoking it by using the `n` option to check for potential conflicts.
  ```shell
  stow -nvSt ~ zsh qtile
  ```
  3. Remove the `n` option and `stow` the packages you want to have.
  ```shell
  stow -vSt ~ zsh qtile
  ```

- ### Install packages from my packages list
  - Install all packages (with an AUR helper)
  ```shell
  yay -S < packages.list
  ```
  - Only install pacman packages
  ```shell
  sudo pacman -S $(comm -12 <(pacman -Slq | sort) <(sort packages.list))
  ```
  - Uninstall packages not listed in the packages list
  ```shell
  sudo pacman -Rsu $(comm -23 <(pacman -Qq | sort) <(sort packages.list))
  ```

- ### Unstow packages from your $HOME (remove symlinks)
  1. `cd` into the cloned dotfiles directory.
  2. Unstow the packages you want to have removed (simulate the operation by using the `n` option once again before unstowing).
  ```shell
  stow -vDt ~ zsh qtile
  ```
