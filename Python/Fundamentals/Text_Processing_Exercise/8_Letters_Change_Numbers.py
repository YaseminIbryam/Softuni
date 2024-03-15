from string import ascii_lowercase
from string import ascii_uppercase


def front_letter(number, letter):
    if letter.isupper():
        return number / (ascii_uppercase.index(letter) + 1)
    elif letter.islower():
        return number * (ascii_lowercase.index(letter) + 1)


def letter_after(letter):
    if letter.isupper():
        return result - (ascii_uppercase.index(letter) + 1)
    elif letter.islower():
        return result + (ascii_lowercase.index(letter) + 1)


result = 0
strings = input().split()
for string in strings:
    first_letter = string[0]
    last_letter = string[-1]
    number = int(string[1:-1])
    result += front_letter(number, first_letter)
    result = letter_after(last_letter)
print(f'{result:.2f}')
