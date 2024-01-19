# string = input()
# list_capital_letter_indices = []
# for index, char in enumerate(string):
#     if char.isupper():
#         list_capital_letter_indices.append(index)
# print(list_capital_letter_indices)
word = input()
print([x for x in range(len(word)) if word[x].isupper()])
# It's saying print all these in list; print x; x comes from for x in range(len(word); and print x if word[x].isupper()
