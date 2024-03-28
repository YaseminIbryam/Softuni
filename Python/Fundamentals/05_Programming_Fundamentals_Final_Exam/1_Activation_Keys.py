def contains(substring: str):
    if substring in activation_key:
        print(f"{activation_key} contains {substring}")
    else:
        print('Substring not found!')


def flip(case: str, start_index: int, end_index: int):
    substring = activation_key[start_index:end_index]
    if case == 'Upper':
        key = activation_key.replace(substring, substring.upper())
    else:  # elif case == 'Lower':
        key = activation_key.replace(substring, substring.lower())
    return key


def slice_(start_index: int, end_index: int):
    key = activation_key[: start_index] + activation_key[end_index:]
    return key


activation_key = input()
while True:
    command_list = input().split('>>>')
    command = command_list[0]
    if command == 'Generate':
        break
    if command == 'Contains':
        contains(command_list[1])
    elif command == 'Flip':
        activation_key = flip(command_list[1], int(command_list[2]), int(command_list[3]))
        print(activation_key)
    elif command == 'Slice':
        activation_key = slice_(int(command_list[1]), int(command_list[2]))
        print(activation_key)
print(f"Your activation key is: {activation_key}")
