words = ['abc', 'xyz']
word = 'sss'


combined = ''
new_list = words[:]
new_list.append(word)
print(new_list)
for i in words:
    combined = combined + i



combination = ''
for j in new_list:
    combination = combination + j
    
print(combination)

l = [11, 12, 13]

print(l[0:2])
print(l[:2])

print(l[1:])
print(l[:])

joinwords = ['abc', 'xyz']
joinword = 'sss'

new_list = joinwords[:]
new_list.append(joinword)
print(new_list)

combined = ''.join(new_list)
print(combined)