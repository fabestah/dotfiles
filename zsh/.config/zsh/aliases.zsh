#!/bin/sh


### SIMPLE ALIASES ###

# Applications
alias hollywood="hacking"
alias lg='lazygit'
alias lv='lvim'
alias code='vscodium'

# Quick Access to Files
alias .zsh="$EDITOR $HOME/.zshrc"
alias sc="source $HOME/.zshrc"

# Customized Listing
alias la='LC_COLLATE=C ls -vAF'
alias lla='LC_COLLATE=C ls -lqvhAF'

# Pacman (Package Management)
alias update-mirrors='rate-mirrors --allow-root --protocol https arch | sudo tee /etc/pacman.d/mirrorlist'

# Get Stuff
alias getsize="sudo du -hc --max-depth=0"
alias getfs="df -PTh"

# System Controls
alias reboot='sudo reboot'
alias shutdownnow='shutdown +0'

# Refresh/Fix Keys
alias archlinx-fix-keys="sudo pacman-key --init && sudo pacman-key --populate archlinux && sudo pacman-key --refresh-keys"

# Systemd
alias mach_list_systemctl="systemctl list-unit-files --state=enabled"

# Copy, Move & Remove
alias cp="cp -iv"
alias mv='mv -iv'
alias rm='rm -iv'

# Colorize Grep Output
alias grep='grep --color=auto'
alias egrep='egrep --color=auto'
alias fgrep='fgrep --color=auto'


### SUFFIX ALIASES ###

# Program Mapping for File Extensions (e.g. test.md)
alias -s {py,rs,ts,js,html,css}=vscodium
alias -s md=glow