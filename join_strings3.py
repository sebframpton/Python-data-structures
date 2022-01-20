from itertools import zip_longest

l1 = ['bbb', 'ccc', None]
l2 = ['xxx', 'yyy', '', 'aaa']

l3 = []

for i in l1:
    if i != None:
        l3.append(i)
l4 = ''.join(l3)
zipped = list(zip_longest(l3, l2))
print(zipped)
print(l3)
print(l4)


s = ''.join(l2)

print(s)