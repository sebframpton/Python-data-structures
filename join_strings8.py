from itertools import zip_longest

f1 = '''\
aaa
bbb
ccc
'''

f2 = '''\
aa
bb
'''


# [('aaa\n'),('bbb\n'),('ccc\n'),('aa\n'),('bb\n')]
f3 = [f1]
# f3 should contain a list string like this ['aaa\nbbb\nccc\n']

f4 = [f2]
# f4 should contain a list string like this ['aa\nbb\n']
f5 = [f3, f4]
print(f5)
# zip longest f3 and f4 [('aaa\nbbb\nccc\n', 'aa\nbb\n')]
print(f3)
print(f4)
# [['']]
new_list = list(zip_longest(f3, f4))


s = ''

for i in new_list:
    for j in i:
        s = s + j
    print(s)

print(new_list)

expected_format = '''\
aaa aa
bbb bb
ccc
'''

expected_format2 = '''\
aa aaa
bb bbb
   ccc
'''
