
# You are making a program to analyze text.
# Take the text as the first input and a letter as the second input,
# and output the frequency of that letter in the text as a whole percentage.
# your code goes here

# The letter l appears 2 times in the text hello,
# which has 5 letters. So,
# the frequency would be (2/5)*100 = 40.

x = input()
z = input()
b = len(x)
y = x.count(z)
result = (y / b * 100)
print(int(result))


# Division result is a float. Use the int() function to convert the result to an integer.
