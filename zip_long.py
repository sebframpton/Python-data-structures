from itertools import zip_longest

l = [1, 2, 3]
l2 = [10, 11, 12, 13]

new_list = list(zip_longest(l, l2))

print(new_list)