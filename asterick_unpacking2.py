from itertools import zip_longest

s = ['one\ntwo\nA\nB', 
'three\nfour','five\nsix\nC', 'seven\neight']
l = []
for i in s:
    x = i.splitlines()
    l.append(x)
print(l)

new_list = list(zip_longest(*l))
print(new_list)
s = ''
for k in new_list:
    for t in k:
        if t == None:   
            s = s + " "
        else:
            s = s + str(t) + ' '
            
    s = s + '\n'
print(s)
    

expected_result = ''' one three five  seven 
                      two four  six   eight
                       A         C
                       B 
                            
                      '''

