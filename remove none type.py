# Remove none type from tuple
# and zip or join them together 

l1 = ("string1","string3","string5", None)
l2 = ("string2","string4","string6")

l3 = []

for i in l1:
    if i != None:
        l3.append(i)
    
l4 = ''.join(l3)
l5 = l4.splitlines()
print(l5)
