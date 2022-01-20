from join_strings6 import removenone
from itertools import zip_longest

x =["1", "2"]
lx = ["ab", "bc", "cd"]
ly = ["string1", "string2", "string3", "string4"]

lz = [x,lx,ly]
zip1 = list(zip_longest(*lz))
print(zip1)
zipped = list(zip_longest(lx, x))

print(removenone(zip1), "zip1")
print(removenone(zipped), "zip")

zipped1 = list(zip_longest(ly,lx))

print(removenone(zipped1), "zipped")
