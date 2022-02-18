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

f3 = [f1]
f4 = [f2]
print(f3)
print(f4)
new_list = list(zip_longest(f3, f4))

s = ''
'''
for i in new_list:
    for j in i:
        s = s + j
    print(s)
'''
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
