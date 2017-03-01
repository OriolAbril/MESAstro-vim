"select files which sould have inlist syntax
au BufRead,BufNewFile inlist set filetype=inlist 
au BufRead,BufNewFile inlist_* set filetype=inlist
"au BufRead,BufNewFile inlist* set filetype=inlist "is not used because it also sets inlist syntax highlight for inlist.vim files. It can be uncommented if desired
au BufRead,BufNewFile *.defaults set filetype=inlist "the three .defaults files are also set to this syntax highlight
