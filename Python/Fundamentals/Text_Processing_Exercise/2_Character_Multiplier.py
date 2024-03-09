first_str, second_str = input().split()
length = max(len(first_str), len(second_str))
result = 0
for i in range(length):
    try:
        result += ord(first_str[i]) * ord(second_str[i])
    except IndexError:
        try:
            result += ord(first_str[i])
        except IndexError:
            result += ord(second_str[i])
print(result)