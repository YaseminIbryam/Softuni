message = input().split()
for index, word in enumerate(message):
    digits = [char for char in word if char.isdigit()]
    str_digits = "".join(digits)
    letter = chr(int(str_digits))
    word = word.replace(str_digits, letter)
    word_list = [char for char in word]
    word_list[-1], word_list[1] = word_list[1], word_list[-1]
    print(''.join(word_list), end=' ')


