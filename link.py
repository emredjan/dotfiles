#!/usr/bin/env python

import os
import platform
import shutil

system = platform.system()
home = os.path.expanduser('~')
dotdir = os.getcwd()

if system == 'Darwin':
    shutil.copyfile(dotdir + '/' + '.gitconfig_mac', dotdir + '/' + '.gitconfig')
elif system == 'Linux':
    shutil.copyfile(dotdir + '/' + '.gitconfig_linux', dotdir + '/' + '.gitconfig')

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

