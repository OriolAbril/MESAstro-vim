import re

keypat=re.compile(r'\s*([^\s!:()]+)\s*=',re.IGNORECASE)
boolpat=re.compile(r'\s*([^\s!:()]+)\s*=\s*.(true|false).',re.IGNORECASE)
intpat=re.compile(r'\s*([^\s!:()]+)\s*=\s*[0-9\-d\.]+',re.IGNORECASE)
matpat=re.compile(r'\s*([^\s!]+)\([:0-9]\)\s*=',re.IGNORECASE)
fd=open('controls.keywords','w')
keys=set()
mats=set()
bols=set()
ints=set()
##controls.defaults
f1=open('controls.defaults','r')
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
f2=open('star_job.defaults','r')
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
f3=open('pgstar.defaults','r')
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
fd.close()
