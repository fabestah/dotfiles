#!/bin/sh


### Simple aliases

# Configs quick access
alias .zsh="$EDITOR $HOME/.zshrc"
alias sc="source $HOME/.zshrc"

# Colorize grep output (good for log files)
alias grep='grep --color=auto'
alias egrep='egrep --color=auto'
alias fgrep='fgrep --color=auto'

# Pacman (package management)
alias update-mirrors='rate-mirrors --allow-root --protocol https arch | sudo tee /etc/pacman.d/mirrorlist'

# Customized listing
alias la='LC_COLLATE=C ls -vAF'
alias lla='LC_COLLATE=C ls -lqvhAF'

# Confirm before overwriting something
alias cp="cp -iv"
alias mv='mv -iv'
alias rm='rm -iv'

# Get size
alias getsize="sudo du -hc --max-depth=0"
alias getfs="df -PTh"

# Hollywood hacking
alias hollywood="hacking"

# Git (lazygit)
alias lg='lazygit'

# LunarVim
alias lv='lvim'

# Codium
alias code='vscodium'

# System controls
alias reboot='sudo reboot'
alias shutdownnow='shutdown +0'

# For when keys break
alias archlinx-fix-keys="sudo pacman-key --init && sudo pacman-key --populate archlinux && sudo pacman-key --refresh-keys"

# systemd
alias mach_list_systemctl="systemctl list-unit-files --state=enabled"


### Suffix Aliases

# Open file type with a particular program (just by typing the filename like test.md)
alias -s {py,rs,ts,js,html,css}=vscodium
alias -s md=glow

### Functions

