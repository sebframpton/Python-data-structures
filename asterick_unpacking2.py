s = ['one\ntwo',
'three\nfour',]

s1 = s[0].splitlines()
s2 = s[1].splitlines()

print(list(zip(s1, s2)))

s = ['one\ntwo',
'three\nfour',]

s1 = s[0].splitlines()
s2 = s[1].splitlines()
l = [s1 + s2]

print(list(zip(l)))