#!/usr/bin/env python

import os

home = os.path.expanduser('~')
dotdir = os.getcwd()

dotfiles = ['.gitconfig',
            '.Rprofile',
            '.tmux.conf',
            '.jupyter/custom/custom.css',
            '.config/nvim/init.vim']

dotlinks = [(dotdir + '/' + d, home + '/' + d) for d in dotfiles]

for src, dst in dotlinks:

    if os.path.islink(dst) or os.path.isfile(dst):
        os.remove(dst)

    os.symlink(src, dst)

