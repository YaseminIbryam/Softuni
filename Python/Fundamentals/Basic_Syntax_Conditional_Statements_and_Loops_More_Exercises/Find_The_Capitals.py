string = input()
list_capital_letter_indices = []
for index, char in enumerate(string):
    if char.isupper():
        list_capital_letter_indices.append(index)
print(list_capital_letter_indices)
