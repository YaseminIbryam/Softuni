string = input()
new_string = f'{string[0]}'
for char in string:
    if char != new_string[-1]:
        new_string += char
print(new_string)