from itertools import zip_longest

l = ['abc', 'xyz', '123', 'aaa']

multiline = ''



for word in l:
    multiline = multiline + word + '\n'
    split_list = word.split()
    print(split_list)

print(multiline + "words")

zipped = list(zip_longest(l))

print(zipped)