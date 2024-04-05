string = input()
indexes = list()
for index, char in enumerate(string):
    if char == '(':
        indexes.append(index)
    elif char == ')':
        print(string[indexes.pop():index+1])
