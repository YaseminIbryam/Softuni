string = input()
value = 0
for letter in string:
    if letter == "a":
        value += 1
    elif letter == "e":
        value += 2
    elif letter == "i":
        value += 3
    elif letter == "o":
        value += 4
    elif letter == "u":
        value += 5
print(value)
