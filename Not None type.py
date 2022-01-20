l1 = ("string1","string3","string5", None)
l2 = ("string2","string4","string6")

l3 = []

for i in l1:
    print(type(i), "type i")
    print(i == type,"i == type")
    print(i, "i")
    print(type, "type")
    if i != None:
        l3.append(i)
    
print(l3)
