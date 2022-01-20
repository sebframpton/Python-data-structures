def put_operator_in_front(h):
    a = h.replace('+', '')
    adding = '+' + a
    return adding

line = put_operator_in_front('+ 8')
line2 = put_operator_in_front('         + 8')
line3 = put_operator_in_front('         8       +')
print('|' + line + '|')
print('|' + line2 + '|')
print('|' + line3 + '|')