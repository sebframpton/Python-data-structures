tt = [
    [True, False, False],
    [False, True, False],
    [False, True, True],
]
a = "o"
b = "x"
s = ''
for i in tt:
    for j in i:
        if j == True:
            s = s + a
        else:
            s = s + b
    s = s + '\n'
print(s)
     
expected_format = '''
    oxo
    xox 
    xoo
'''
