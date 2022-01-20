words = ["dog", "chopsticks", "candy", "on"]
w = []

def numSpaces(num):
    spaces = ""
    for j in range(num):
        spaces = spaces + " "
    #print("|" + spaces + "|")
    return spaces

for i in words:
    w.append(len(i))
highiest_num = max(w)
print(highiest_num)

for k in words:
    a = highiest_num - len(k)
    print(numSpaces(a)+k)

 #   newline = "\n"
  #  c =  b + words[0] + newline +  b + words[1]
#print(c)
#for word in words:
  #  print()