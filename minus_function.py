def minus(a, b):
    return a - b


print(minus(1, 3))

l = [1, 3]
print(minus(*l))


print(minus(*[1,3]))

print(minus(1, 3))

l = [1, 3]
print(minus(*l))

print(list(zip(["1","3"],["2","4"],['abc',"xyz"])))

l2 = [["1","3"],["2","4"],['abc',"xyz"]]
print(*l2)
print(list(zip(*l2)))