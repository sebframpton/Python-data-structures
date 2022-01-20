# Given a sentence as input,
# calculate and output the average word length of that sentence.
# To calculate the average word length, you need to divide the
# sum of all word lengths by the number of words in the sentence.

# Python program to convert a list to string


# Driver code
text = input()


a = text.split()
print(len(a))
# using list comprehension
listToStr = ''.join([str(elem) for elem in a])
b = len(listToStr) / len(a)
print(len(listToStr))
print(listToStr)
print(b)


# Sample Input
# this is some text

# Sample Output
# 3.5
# Explanation: There are 4 words in the given input,
# with a total of 14 letters, so the average length will be: 14/4 = 3.5

# Strings have a split() method, which returns the string split into a list,
# with the given separator. By default, the separator is a space, so calling split()
# will return a list containing the words of the string as items.
