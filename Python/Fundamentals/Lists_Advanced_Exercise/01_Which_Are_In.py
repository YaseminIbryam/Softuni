list_1 = input().split(", ")
list_2 = input().split(", ")
# substrings = []
# for string_1 in list_1:
#     for string_2 in list_2:
#         if string_1 in string_2:
#             substrings.append(string_1)
#             break
# print(substrings)
print([string_1 for string_1 in list_1 if any(string_1 in string_2 for string_2 in list_2)])