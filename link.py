#!/usr/bin/env python

import os

home = os.path.expanduser('~')
dotdir = os.getcwd()

dotfiles_home = ['.gitconfig',
                 '.Rprofile',
                 '.tmux.conf']

dotlinks_home = [(dotdir + '/' + d, home + '/' + d) for d in dotfiles_home]

dotlinks_other = [(dotdir + '/jupyter/custom.css', home + '/.jupyter/custom/custom.css'),
                  (dotdir + '/nvim/init.vim', home + '/.config/nvim/init.vim')]

dotlinks = dotlinks_home + dotlinks_other

for src, dst in dotlinks:

    if os.path.islink(dst) or os.path.isfile(dst):
        os.remove(dst)

    os.symlink(src, dst)

