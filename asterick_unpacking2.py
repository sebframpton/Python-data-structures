s = ['one\ntwo',
'three\nfour',]

s1 = s[0].splitlines()
s2 = s[1].splitlines()

print(list(zip(s1, s2)))

s = ['one\ntwo',
'three\nfour','five\nsix', 'seven\neight']
l = []
for i in s:
    x = i.splitlines()
    l.append(x)
print(l)
#l = [['one','two'],['three', 'four'],['five', 'six']]
#print(l)
print(list(zip(*l)))

#[['one', 'three',]['two','four']]

#s1['one', 'two']
#s2['three', 'four']

