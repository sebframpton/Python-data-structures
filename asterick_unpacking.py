s1 = 'one\ntwo'
s2 = 'three\nfour'

sp1 = s1.splitlines()
sp2 = s2.splitlines()

print(list(zip(sp1, sp2)))

s = ['one\ntwo',
'three\nfour']

sp4 = list(zip("one\n"))
print(sp4)

'''
nl = list(zip(["x",'y',"z"],["7","8","9"]))
print(nl)
[("one","three"), ("two", "four")]
[('a', '1'),('b','2'),('c','3')]

[('abc', '123', 'bbb'), ('xyz', 'zzz', 'ccc')]

n1 = list(zip(['x1', 'y2'], ['w7', 'v8'], ['a1', 'a2']))
print(n1)

n2 = list(zip(['1', 'a', 'y'],['2', 'x', 'b']))
print(n2)

[("w1", "x3"), ("w2","x5")]

'''