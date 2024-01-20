lines = int(input())
word = input()
all_strings = []
filtered_list = []
for line in range(lines):
    string = input()
    all_strings.append(string)
print(all_strings)
for string in all_strings:
    if word in string:
        filtered_list.append(string)
print(filtered_list)