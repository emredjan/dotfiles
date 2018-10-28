alias cuc="conda update conda"
alias cua="conda update --all"
alias cca="conda clean --all"
alias cuf="conda update -c conda-forge $(conda list | grep "conda-forge" | awk '{print $1}' | tr '\n' ' ')"

alias clr="clear"

alias cd..="cd .."
alias ..="cd .."
alias ...="cd ../.."

alias jserve="bundle exec jekyll serve --watch --host 0.0.0.0"
alias ca="conda activate"
alias cb="conda activate base"
alias cx="conda deactivate"
alias jn="jupyter notebook"
alias jl="conda activate base && jupyter lab"

alias zshreload="source ~/.zshrc"

alias lst="ls -ltrh"

