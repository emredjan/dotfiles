call plug#begin('~/.local/share/nvim/plugged')

Plug 'scrooloose/syntastic'
Plug 'tpope/vim-surround'
Plug 'ervandew/supertab'
Plug 'vim-airline/vim-airline'
Plug 'vim-airline/vim-airline-themes'
Plug 'kien/ctrlp.vim'
Plug 'flazz/vim-colorschemes'
Plug 'tmux-plugins/vim-tmux'
Plug 'christoomey/vim-tmux-navigator'
Plug 'plasticboy/vim-markdown'
Plug 'cjrh/vim-conda'
Plug 'valloric/youcompleteme'
Plug 'scrooloose/nerdtree'
Plug 'wincent/terminus'
Plug 'chiel92/vim-autoformat'

call plug#end()

syntax enable
set background=dark
colorscheme materialtheme
set t_Co=256
set encoding=utf8
set number
set tabstop=8 softtabstop=0 expandtab shiftwidth=4 smarttab

" Toggle nerdtree with F10
map <F10> :NERDTreeToggle<CR>

" Current file in nerdtree
map <F9> :NERDTreeFind<CR>

let g:airline_powerline_fonts = 1
let g:airline_symbols_ascii = 0
let g:airline_theme='onedark'
let g:vim_markdown_folding_disabled = 1
let g:ycm_python_binary_path = 'python'
let g:conda_startup_msg_suppress = 1
let g:python3_host_prog = '/usr/local/bin/python3'
let g:loaded_python_provider = 1
let NERDTreeShowHidden=1

highlight Pmenu ctermfg=232 ctermbg=252 guifg=#ffffff guibg=#3a3a3a
highlight PmenuSel ctermfg=252 ctermbg=235 guifg=#ffffff guibg=#3a3a3a
