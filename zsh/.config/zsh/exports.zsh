#!/bin/sh
HISTSIZE=1000000
SAVEHIST=1000000

export EDITOR="codium"
export TERMINAL="kitty"
export BROWSER="brave"
export PATH="$HOME/.local/bin":$PATH
export MANPAGER='nvim +Man!'
export MANWIDTH=999

export PATH=$HOME/.config/zsh:$PATH
export PATH=$HOME/.cargo/bin:$PATH
export PATH=$HOME/.local/share/go/bin:$PATH
export GOPATH=$HOME/.local/share/go
export PATH=$HOME/.fnm:$PATH
export PATH="$HOME/.local/share/neovim/bin":$PATH

export QUOTING_STYLE=literal
export $(dbus-launch) # keyring functionality for codium github login
eval "$(zoxide init zsh)"
