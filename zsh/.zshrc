#!/bin/sh
# Configs quick access
alias nvimrc=#!/bin/sh
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

# History
HISTFILE=~/.zsh_history

# Prompt theme
plug "zap-zsh/zap-prompt"

# Keybinds
bindkey -v

export PATH="$HOME/.local/bin":$PATH'nvim ~/.config/nvim/'
