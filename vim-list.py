import re

keypat=re.compile(r'\s*!?([^!\s#-]+)',re.IGNORECASE)
elempat=re.compile(r'\s*([0-9]{1,3})([a-z]{1,2})',re.IGNORECASE)
keys=set()
els=set()
fd=open('list.vim','w')

# Write start of .vim file
fd.write('if exists("b:current_syntax")\n   finish\nendif\n\n"Known elements\nsyntax case ignore\n')

# get and write all known elements
f1=open('all_known_elements.txt','r')
for line in f1:
    raw_els=line.split(',')
    writeln='syntax keyword listElement'
    pint=False
    for el in raw_els:
        m=elempat.match(el)
        if m:
            pint=True
            nice_el=m.groups(1)[1].lower()+m.groups(1)[0]
            els.add(nice_el)
            writeln+=' '+nice_el
    if pint:
        fd.write(writeln+'\n')
f1.close()

## get keywords for histroy files
f1=open('/home/oriol/mesa-r9575/star/defaults/history_columns.list','r')

for line in f1:
    m=keypat.match(line)
    if m:
        key=m.groups(1)[0]
        if (key!='mixing_regions' and key!='mix_relr_regions' and key!='burning_regions' and
            key not in els):
            keys.add(key)
f1.close()

## get keywords for profile files
f1=open('/home/oriol/mesa-r9575/star/defaults/profile_columns.list','r')
for line in f1:
    m=keypat.match(line)
    if m:
        key=m.groups(1)[0]
        if (key!='mixing_regions' and key!='mix_relr_regions' and key!='burning_regions' and
            key not in els):
            keys.add(key)
f1.close()

# write keywords in list.vim
fd.write('\n"Keywords\nsyntax case ignore\n')
for key in keys:
    string='syntax keyword listKeyword '+key+'\n'
    fd.write(string)

#Add special keywords, comments and integers
fd.write('syntax match listKeyword /\zsmixing_regions\ze\s\+[0-9]\+/\n')
fd.write('syntax match listKeyword /\zsmix_relr_regions\ze\s\+[0-9]\+/\n')
fd.write('syntax match listKeyword /\zsburning_regions\ze\s\+[0-9]\+/\n')
fd.write('\n"Comments\nsyntax match listComment "'+r'\v'+'!.*$"\n')
fd.write('\n"Integers\nsyntax match listNumber /\s\+[0-9]\+/\n')
fd.write('\n"Set higlight type to the defined keywords\nhighlight link listElement Special\n')
fd.write('highlight link listKeyword Keyword\n')
fd.write('highlight link listComment Comment\n')
fd.write('highlight link listNumber Number\n')
fd.write('let b:current_syntax = "list"')

fd.close()
