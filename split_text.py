text = '    + xyz'
print(text)
split_text = text.split("+")
print(split_text)
join_text = ''.join(split_text)
add_plus = '+' + join_text
print(add_plus, "joined text")
final_text = '+     xyz'
print(final_text)

a = text.replace('+', '')
b = '+' + a
print(b)