# MESAstro-vim 
## Release 9575
Set of files to place in `$HOME/.vim/` in order to enable syntax highlight for MESA (release 9575, for other releases see below) inlist and \*.list files. It highlights all the possible keywords (only if followed by an apropiate expression if it is either a boolean or a number) as well as comments.

Fo the syntax highlight to work properly. the `.vimrc` file should contain the lines:
```
syntax on
filetype indent plugin on
```
The \*.vim files found in `syntax/` directory, have each section commented, therefore can be easily modified to delete syntax highlight for numbers or strings. 

The \*.vim files found in `ftplugin/` directory modify the configuration of tabs to expandtab and tablength eual to 3 spaces and set autoindent on.

## Other MESA releases

The repository also contains the files `vim-inlist.py` and `vim-list.py` written in Python that write the inlist.vim and list.vim files when executed by retreving the keywords from `$MESA_DIR/star/defaults` (note that it is required to have `$MESA_DIR` properly defined). This newli written files can then be used to replace the current files in the syntax folder, enabling syntax highlight for any MESA release (as long as the filenames of the defaults are the same and follow the same pattern of commenting the keywords without a space after the `!` while comments do).
