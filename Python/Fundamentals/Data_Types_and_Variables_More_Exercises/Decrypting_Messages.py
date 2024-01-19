key = int(input())
lines = int(input())
for line in range(lines):
    letter = input()
    ascii_letter = ord(letter)
    ascii_letter += key
    letter_for_message = chr(ascii_letter)
    print(letter_for_message, end='')