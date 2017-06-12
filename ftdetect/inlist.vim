"select files which sould have inlist syntax
au BufRead,BufNewFile inlist* set filetype=inlist "use inlist syntax for any file whose name starts with inlist
au BufRead,BufNewFile inlist.vim set filetype=vim "override previous behavious only for inlist.vim file
au BufRead,BufNewFile *.defaults set filetype=inlist "the three .defaults files are also set to this syntax highlight
