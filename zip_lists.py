from itertools import zip_longest
l = [['words1','words4'],['words2','words5'],['words3','words6'],['oneword']]

zipped = zip_longest(*l)
#print(list(zipped))
line1 = ('')
line2 = []
for i in zipped:
    line2.append(i)
  

print(line2)
    #line3 = line1 + i
#print(line3)
