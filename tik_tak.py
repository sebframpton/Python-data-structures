tt = [True, False, False]
a = "o"
b = "x"
s = ''
for i in tt:
    if i == True:
        s = s + a
    else:
        s = s + b
print(s)
     

expected_format = 'oox'