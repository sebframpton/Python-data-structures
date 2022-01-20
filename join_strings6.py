def removenone(x):
    l4 = []
    for i in x:
        l5 = []
        for j in i:
            if j != None:
                l5.append(j + " ")
            else:
                l5.append("")
        l4.append(l5)
        print(l5, "L5")
    combined = ''
    for k in l4:
    
        l6 = "".join(k)
        combined = combined + l6 + "\n"
        print(l6, "l6")
    return combined