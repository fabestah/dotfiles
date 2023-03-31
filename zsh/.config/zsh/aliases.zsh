#!/bin/sh
# Configs quick access
alias .nvim='lvim ~/.config/nvim/'
alias .qtile='cd ~/.config/qtile/'
alias qkeys= 'code /home/fabestah/.config/qtile/core/keys'
alias /lvim='lvim ~/.config/lvim/config.lua'

# Colorize grep output (good for log files)
alias grep='grep --color=auto'
alias egrep='egrep --color=auto'
alias fgrep='fgrep --color=auto'

# Pacman (package management)
alias update-mirrors='rate-mirrors --allow-root --protocol https arch | sudo tee /etc/pacman.d/mirrorlist'

# Customized listing
alias la='LC_COLLATE=C ls -vAF'
alias lla='LC_COLLATE=C ls -lqvAF'

# Confirm before overwriting something
alias cp="cp -i"
alias mv='mv -i'
alias rm='rm -i'

# Get size
alias getsize="sudo du -hc --max-depth=0"

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
