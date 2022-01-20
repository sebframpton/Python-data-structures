from itertools import zip_longest
l1 = ['1', '2', '3']
l2 = ["a", "b","c", "d"]
lx = ["ab", "bc", "de"]

l3 = list(zip_longest(l1,l2))
l4 = []

def removenone(x):
    
    for i in l3:
        l5 = []
    # print(type(i[0]),i)
        for j in i:
            if j != None:
                l5.append(j)
            else:
                l5.append("")
        l4.append(l5)
    combined = ''
    for k in l4:
    
        l6 = "".join(k)
        combined = combined + l6 + "\n"
    return combined

print(removenone())  