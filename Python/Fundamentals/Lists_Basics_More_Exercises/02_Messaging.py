indexes = [sum(int(digit) for digit in str(number)) for number in (list(map(int, input().split())))]
string = list(input())
message = []
for index in indexes:
    while index >= len(string):
        index -= len(string)
    message.append(string.pop(index))
print(''.join(message))

