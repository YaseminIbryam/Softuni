import math
import sys
strongest_word_ascii = -sys.maxsize
strongest_word = " "
command = input()
while command != "End of words":
    sum_ascii = 0
    word = command
    for index, letter in enumerate(word):
        sum_ascii += ord(letter)
    low_first_letter = word[0].lower()
    if low_first_letter != 'a' and low_first_letter != 'e' and \
            low_first_letter != 'i' and low_first_letter != 'o' and low_first_letter != 'u' and low_first_letter != 'y':
        sum_ascii = math.floor(sum_ascii / len(word))
    else:
        sum_ascii *= len(word)
    if sum_ascii > strongest_word_ascii:
        strongest_word = word
        strongest_word_ascii = sum_ascii
    command = input()

print(f"The most powerful word is {strongest_word} - {strongest_word_ascii}")

