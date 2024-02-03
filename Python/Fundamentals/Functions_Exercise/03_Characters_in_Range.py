def find_chars_between(str1, str2):
    return " ".join([chr(i) for i in range(ord(str1) + 1, ord(str2))])


print(find_chars_between(input(), input()))
