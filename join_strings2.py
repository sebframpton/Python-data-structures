l = (None,None, "string1", "string2", "string3")
l2 = [None,None]

#l3 = ''.join(l)
#print(l + l2)
print(l)
l4 = []
for i in l:
    l4.append("")
    l5 = "".join(l4)

print(l4)
print(l5 + "join string")