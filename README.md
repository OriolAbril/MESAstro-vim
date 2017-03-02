# MESAstro-vim

Set of files to place in `$HOME/.vim/` in order to enable syntax highlight for MESA inlist and \*.list files. It highlights all the possible keywords (only if followed by an apropiate expression if it is either a boolean or a number) as well as comments.

Fo the syntax highlight to work properly. the `.vimrc` file should contain the lines:
```
syntax on
filetype indent plugin on
```
The \*.vim files found in `syntax/` directory, have each section commented, therefore can be easily modified to delete syntax highlight for numbers or strings. 

The \*.vim files found in `ftplugin/` directory modify the configuration of tabs to expandtab and tablength eual to 3 spaces and set autoindent on.
