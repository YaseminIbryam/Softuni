# string = input()
# new_string = ''
# unique_symbols = 0
# index1 = 0
# for index, char in enumerate(string):
#     if char.isdigit():
#         if string[index - 1].isdigit():
#             index1 += 1
#             continue
#         if index != len(string) - 1 and string[index + 1].isdigit():
#                 number = int(string[index:index + 2])
#         else:
#             number = int(char)
#         symbols = string[index1:index]
#         new_string += symbols.upper() * number
#         index1 = index + 1
#     elif char.upper() not in new_string:
#         unique_symbols += 1
# print('Unique symbols used:', unique_symbols)
# print(new_string)

text = input()
rage_message = ""
repetitions = ""
sub_string = ""
for index in range(len(text)):
    if not text[index].isdigit():  # non-numeric symbol
        sub_string += text[index].upper()
    else:  # number of repetitions
        for next_symbols in range(index, len(text)):
            if not text[next_symbols].isdigit():
                break
            repetitions += text[next_symbols]
        rage_message += sub_string * int(repetitions)
        repetitions = ""
        sub_string = ""
print(f"Unique symbols used: {len(set(rage_message))}")
print(rage_message)
