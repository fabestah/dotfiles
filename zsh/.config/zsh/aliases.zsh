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
alias update-mirrors='sudo systemctl start reflector.service'

# Get Stuff
alias getfs="df -PTh"
alias getkeys='xev | awk -F"[ )]+" "/^KeyPress/ { a[NR+2] } NR in a { printf \"%-3s %s\n\", \$5, \$8 }"'
alias getsize="sudo du -hc --max-depth=0"

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