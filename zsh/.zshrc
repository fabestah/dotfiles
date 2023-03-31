#!/bin/sh
[ -f "$HOME/.local/share/zap/zap.zsh" ] && source "$HOME/.local/share/zap/zap.zsh"

# Source
plug "$HOME/.config/zsh/aliases.zsh"
plug "$HOME/.config/zsh/exports.zsh"

# Plugins
plug "zap-zsh/supercharge"
plug "zsh-users/zsh-autosuggestions"
plug "zsh-users/zsh-syntax-highlighting"
plug "hlissner/zsh-autopair"
plug "zap-zsh/fzf"
plug "zap-zsh/vim"

# Prompt theme
plug "zap-zsh/zap-prompt"

# Run on startup
pfetch

# History
HISTFILE=~/.config/zsh/.zsh_history

# Keybinds
bindkey -v

export PATH="$HOME/.local/bin":$PATH'nvim ~/.config/nvim/'
