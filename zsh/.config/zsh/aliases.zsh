#!/bin/sh
# Configs quick access
alias nvimrc='lvim ~/.config/nvim/'
alias lvimrc='lvim ~/.config/lvim/config.lua'
alias qtilecfg='cd ~/Projects/dotfiles/qtile/.config/qtile/'

# Colorize grep output (good for log files)
alias grep='grep --color=auto'
alias egrep='egrep --color=auto'
alias fgrep='fgrep --color=auto'

# Pacman (package management)
alias update-mirrors='rate-mirrors --allow-root --protocol https arch | sudo tee /etc/pacman.d/mirrorlist'

# List every file colorized automatically
alias ls='ls --color=auto'
alias lsa='ls -a'

# Confirm before overwriting something
alias cp="cp -i"
alias mv='mv -i'
alias rm='rm -i'

# Git (lazygit)
alias lg='lazygit'

# LunarVim
alias lv='lvim'

# Codium
alias codium='code'

# System controls
alias reboot='sudo reboot'
alias shutdownnow='shutdown +0'

# For when keys break
alias archlinx-fix-keys="sudo pacman-key --init && sudo pacman-key --populate archlinux && sudo pacman-key --refresh-keys"

# systemd
alias mach_list_systemctl="systemctl list-unit-files --state=enabled"
