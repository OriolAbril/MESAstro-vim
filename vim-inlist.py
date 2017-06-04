import re,os

keypat=re.compile(r'\s*([^\s!:()]+)\s*=',re.IGNORECASE)
boolpat=re.compile(r'\s*([^\s!:()]+)\s*=\s*.(true|false).',re.IGNORECASE)
intpat=re.compile(r'\s*([^\s!:()]+)\s*=\s*[0-9\-d\.]+',re.IGNORECASE)
matpat=re.compile(r'\s*([^\s!]+)\([:0-9]\)\s*=',re.IGNORECASE)
fd=open('inlist.vim','w')
folder=os.environ['MESA_DIR']+'/star/defaults/'
keys=set()
mats=set()
bols=set()
ints=set()

##controls.defaults
f1=open(folder+'controls.defaults','r')
for line in f1:
    b=boolpat.match(line)
    i=intpat.match(line)
    if b:
        bols.add(b.groups(1)[0])
    elif i:
        ints.add(i.groups(1)[0])
    else:
        m=keypat.match(line)
        if m:
            keys.add(m.groups(1)[0])
    n=matpat.match(line)
    if n:
        mats.add(n.groups(1)[0])
f1.close()

##star_job.defaults
f2=open(folder+'star_job.defaults','r')
for line in f2:
    b=boolpat.match(line)
    i=intpat.match(line)
    if b:
        bols.add(b.groups(1)[0])
    elif i:
        ints.add(i.groups(1)[0])
    else:
        m=keypat.match(line)
        if m:
            keys.add(m.groups(1)[0])
    n=matpat.match(line)
    if n:
        mats.add(n.groups(1)[0])
f2.close()

##pgstar.defaults
f3=open(folder+'pgstar.defaults','r')
for line in f3:
    b=boolpat.match(line)
    i=intpat.match(line)
    if b:
        bols.add(b.groups(1)[0])
    elif i:
        ints.add(i.groups(1)[0])
    else:
        m=keypat.match(line)
        if m:
            keys.add(m.groups(1)[0])
    n=matpat.match(line)
    if n:
        mats.add(n.groups(1)[0])
f3.close()

#write inlist.vim
fd.write('if exists("b:current_syntax")\n   finish\nendif\n\n"define keywords (obtained from controls.defaults, star_job.defaults and pgstar.defaults)\
"some of the keywords will only highlight if they are followed by the corresponding boolean or number\nsyntax case ignore\n')

#write obtained keywords in file
for key in keys:
    string='syntax keyword inlistKeyword '+key+'\n'
    fd.write(string)
for bol in bols:
    string=r'syntax match inlistKeyword /\zs'+bol+'\ze\s*=\s*.false./\n'
    fd.write(string)
    string=r'syntax match inlistKeyword /\zs'+bol+'\ze\s*=\s*.true./\n'
    fd.write(string)
for integ in ints:
    string='syntax match inlistKeyword /\zs'+integ+'\ze\s*=\s*[0-9\-d\.]\+/\n'
    fd.write(string)
for mat in mats:
    string=r'syntax match inlistKeyword /\zs'+mat+'\ze([0-9]*)/\n'
    fd.write(string)

fd.write('highlight link inlistKeyword Keyword\n\n"define comments\n')
fd.write(r'syntax match inlistComment "\v!.*$"')
fd.write('\nhighlight link inlistComment Comment\n\n"define the headers of the different sections in an inlist as Identifiers\n')
fd.write('syntax match inlistHeader "\\v\&controls"\nsyntax match inlistHeader "\\v\&star_job"\n')
fd.write('syntax match inlistHeader "\\v^\/"\nsyntax match inlistHeader "\\v\&pgstar"\nhighlight link inlistHeader Identifier\n')
fd.write('\n"Numbers of various sorts\n"" Integers\nsyn match inlistNumber display "\<\d\+\(_\\a\w*\)\=\>"\n')
fd.write('" floating point number, without a decimal point\nsyn match inlistNumber display "\<\d\+[deq][-+]\=\d\+\(_\\a\w*\)\=\>"')
fd.write('\n" " floating point number, starting with a decimal point\nsyn match inlistNumber display "\.\d\+\([deq][-+]\=\d\+\)\=\(_\\a\w*\)\=\>"\n')
fd.write('" " floating point number, no digits after decimal\nsyn match inlistNumber display "\<\d\+\.\([deq][-+]\=\d\+\)\=\(_\\a\w*\)\=\>"\n')
fd.write('" " floating point number, D or Q exponents\nsyn match inlistNumber display "\<\d\+\.\d\+\([dq][-+]\=\d\+\)\=\(_\a\w*\)\=\>"\n')
fd.write('" " floating point number\nsyn match inlistNumber  display "\<\d\+\.\d\+\(e[-+]\=\d\+\)\=\(_\\a\w*\)\=\>"\n')
fd.write('highlight link inlistNumber Number\n\n')
fd.write('"define booleans with the dots\nsyntax match inlistBoolean ".true."\n')
fd.write('syntax match inlistBoolean ".false."\nhighlight link inlistBoolean Boolean\n')
fd.write('"define strings\n')
fd.write(r'''syntax region inlistString start=/\v'/ skip=/\v\\./ end=/\v'/''')
fd.write('\nhighlight link inlistString String\n\n')
fd.write('let b:current_syntax = "inlist"')
fd.close()
