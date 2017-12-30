#!/usr/bin/env python

import os
import platform

system = platform.system()
home = os.path.expanduser('~')
dotdir = os.getcwd()


dotfiles = [('.Rprofile', '.Rprofile'),
            ('.jupyter/custom/custom.css', '.jupyter/custom/custom.css'),
            ('.config/nvim/init.vim', '.config/nvim/init.vim')]

if system == 'Darwin':
    dotfiles_add = [('.gitconfig_mac', '.gitconfig'),
                    ('.tmux.conf_mac', '.tmux.conf'),
                    ('.config/fish/config.fish_mac', '.config/fish/config.fish')]
elif system == 'Linux':
    dotfiles_add = [('.gitconfig_linux', '.gitconfig'),
                    ('.tmux.conf_linux', '.tmux.conf')]

dotfiles += dotfiles_add

dotlinks = [(dotdir + '/' + s, home + '/' + d) for s, d in dotfiles]

for src, dst in dotlinks:

    if os.path.islink(dst) or os.path.isfile(dst):
        os.remove(dst)

    os.symlink(src, dst)

