![Logo](MESA-vim.png)

Set of files to to enable syntax highlight for MESA inlist and \*.list files. It highlights all the possible keywords (only if followed by an apropiate expression if it is either a boolean or a number) as well as comments. The syntax highlight of inlist files is applied to any file whose name starts with inlist except `inlist.vim`.

For the syntax highlight to work properly. the `.vimrc` file should contain the lines:
```
syntax on
filetype indent plugin on
```

The \*.vim files found in `ftplugin/` directory modify the configuration of tabs to expandtab and tablength equal to 3 spaces and set autoindent on.

The \*.vim files found in `syntax/` directory and the ones generated with the python codes have each section commented, therefore can be easily modified to delete syntax highlight for numbers or strings. 

## Release 9575

The \*.vim files found in `syntax/` directory are the ones corresponding to MESA release 9575. Thus, using MESAastro-vim for this release only requires moving the folders `ftdetect/`, `ftplugin/` and `syntax/` inside `$HOME/.vim/`.

## Other MESA releases

The repository also contains the files `vim-inlist.py` and `vim-list.py` written in Python that write the inlist.vim and list.vim files when executed by retreving the keywords from `$MESA_DIR/star/defaults` (note that it is required to have `$MESA_DIR` properly defined). 
The execution of the python codes will create two files `inlist.vim` and `list.vim` which should replace the files currently present in the `syntax/` folder. Afterwards, the three folders should be moved or copied inside `$HOME/.vim/` as explained for MESA-r9575.
The python codes rely on the \*.defaults files and the `history_columns.list` and `profile_columns.list`, therefore, this repository is campatible with any MESA release as long as these filenames remain the same.
