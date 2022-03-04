from itertools import zip_longest


l1 = [1, 2]
l2 = [4, 3, 5]
l3 = [1]
l4 = [2, 3, 4, 5, 5]
 
l = [l1,l2,l3,l4]
print(l)
new_list = list(zip_longest(*l))
print(new_list)
# [(1,3,1,2),(2,34,none,3),(none, 5,none,4),(none,none,none,5)]
var1 = ''
for i in new_list:
    for j in i:
        if j == None:
            var1 = var1 + ' '
        else:   
            var1 = var1 + str(j)
    var1 = var1 + '\n'
print(var1)
    