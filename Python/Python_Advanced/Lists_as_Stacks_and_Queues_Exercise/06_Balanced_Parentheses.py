def is_even(number):
    if number % 2 == 0:
        return True
    return False


parentheses = input()
round = []
square = []
curly = []
are_balanced = True
if len(parentheses) % 2 != 0:
    are_balanced = False
for index, char in enumerate(parentheses):
    if char == '(':
        round.append(is_even(index))
    elif char == ')':
        if is_even(index) == round.pop():
            are_balanced = False
    elif char == '{':
        curly.append(is_even(index))
    elif char == '}':
        if is_even(index) == curly.pop():
            are_balanced = False
    elif char == '[':
        square.append(is_even(index))
    elif char == ']':
        if is_even(index) == square.pop():
            are_balanced = False
    if not are_balanced:
        print('NO')
        break
else:
    print('YES')
