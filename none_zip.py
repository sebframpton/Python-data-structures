from itertools import zip_longest


l1 = [1, 2]
l2 = [3, 4, 5]
l3 = [1]
l4 = [2, 3, 4, 5]
 
l = [l1,l2,l3,l4]

new_list = list(zip_longest(*l))
print(new_list)

for i in new_list:
    if i[0] == None:
        var1 = '' + str(i[1])

    else:   
        var1 = str(i[0]) + str(i[1]) + str(i[2]) + str(i[3])
    print(var1)
    