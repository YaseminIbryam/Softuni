# text = input()
# delete = 0
# index = 0
# for char in text:
#     if char == '>':
#         integer = int(text[index + 1])
#         delete += integer
#     elif delete > 0:
#         for i in range(delete):
#             if text[index] == '>':
#                 break
#             text = f'{text[:index]}{text[index + 1:]}'
#             delete -= 1
#             index -= 1
#     index += 1
# print(text)
some_string = input()
final_string = ""
strength = 0
for index in range(len(some_string)):
    # Explosion
    if strength > 0 and some_string[index] != ">":
        strength -= 1
    # > mark
    elif some_string[index] == ">":
        final_string += some_string[index]
        strength += int(some_string[index + 1])
    # No explosion, no > mark
    else:
        final_string += some_string[index]
print(final_string)
