from itertools import zip_longest
from join_strings6 import removenone
# split list into their own elements and rejoin them to display in string format
# and tab new line each math symbol in each column

# addition = ["32 + 698", "3801 - 2", "45 + 43", "123 + 49"]
# number of spaces function
def numSpaces(num):
    spaces = ""
    for j in range(num):
        spaces = spaces + " "
    #print("|" + spaces + "|")
    return spaces

# Spacing function    
def spacing(formula):
   
    x = formula.split("+")
    y = '\n+'.join(x)
    z = y.split("-")
    j = '\n-'.join(z)
    a = j.split()
    print(j, "j contains")
    print(a, "a contains")
    print(z, "z contains")
    c = []
    calculate = eval(formula)
    cal_len = len(str(calculate))
    for i in a:
        # add to a new list and find the length of each string
        c.append(len(i))
     
    c.append(cal_len)
        
    # get the highiest number in the new list with max function
    
    highiest_num = max(c)
    line = highiest_num * "-" + "--"
    #print(cal_len, "cal length")
    cal_line = highiest_num + 2 - len(str(calculate))
    cal = " " * cal_line

    #print(cal_line, "length of string")
    calculation = cal + str(calculate)
  
    for k in a:

        # loop through the new split list again and
        # take away the length of the new item list 
        # from the highiest number to fill in the space
        sub = highiest_num - len(k)
        space = " " * sub
    
    b = j.splitlines()
    print(b, "check spaces")
    t = []
    s = []
    for r in b:
        stripped_num = r.strip()
        s.append(len(r))
        t.append(r)
        
    adding_up = ''
    for h in b:
        # h = '+ 8 '
        strip_num = h.strip() # '+ 8'
        p = highiest_num + 2 - len(strip_num) # 7 + 2 - 3 = 6
        new_h = numSpaces(p) + h # '     + 8'
        # '      + 8'
        line2 = new_h.replace('+', '') # '       8 '
        line3 = line2.replace('-', '') # line 3 has a new string which replaces + with empty string so - space
        if '+' in new_h:
            line4 = '+'+ line3# '+       8  '
           
        else:
            line4 = line3
        if '-' in new_h:
            line5 = '-' + line4 # if - exist in line 5 add - to the start of the string 
        else:  
            line5 = line4 # else if it doesn't exist line 5 = line 4 which just runs the + at the start of the line 
      
        
        adding_up = adding_up + line5 + "\n" # adding contains '+        8 '
     
        # takeaway contains '      8 ' adding + takeaway = '+         8         8 '
    # return adding up with plus and take away operator from line 5 and add the new string to adding up.   
    return adding_up + line + '\n' + calculation

def arithmetic_formulas(var):
    outside = var
    
    for i in outside:
        print(spacing(i))
    return outside

f1 = ['18+41+8-134+12-14','23+2392942-232','12+2-4+1']
f2 = ''

for i in f1:
    splitline1 = i.splitlines()
    print(splitline1)
    out = spacing(i)
    print(out)

for j in splitline1:
    zipped = list(zip_longest(j))
    print(zipped, "zipped")
#print(f2)
outlines = ''
calculate = eval('18 + 499999 + 8 - 134 + 123913 - 14214')

