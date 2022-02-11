from itertools import zip_longest

l1 = [1,2]
l2 = [3,4,5]
l3 = [l1] + [l2]
print(l3, "l3")
new_list = list(zip_longest(*l3))

print(new_list, "new list")

for i in new_list:
    
    a = a + i
    
    for j in i:
        if j == None:
            var1 = ''
        else:
            var1 = str(j) 
        print(var1)