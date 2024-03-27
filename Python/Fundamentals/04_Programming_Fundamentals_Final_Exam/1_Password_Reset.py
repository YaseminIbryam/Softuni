def take_odd():
    new_string = ''
    for index, char in enumerate(string):
        if index % 2 != 0:
            new_string += char
    return new_string


def cut(index: int, length: int):
    substring = string[index:index+length]
    new_string = string.replace(substring, '', 1)
    return new_string


def substitute_func(substring, substitute):
    if substring in string:
        new_string = string.replace(substring, substitute)
        return new_string



string = input()
while True:
    command_list = input().split()
    command = command_list[0]
    if command == 'Done':
        break
    if command == 'TakeOdd':
        string = take_odd()
    elif command == 'Cut':
        string = cut(int(command_list[1]), int(command_list[2]))
    elif command == 'Substitute':
        string_ = substitute_func(command_list[1], command_list[2])
        if string_:
            string = string_
        else:
            print('Nothing to replace!')
            continue
    print(string)
print(f"Your password is: {string}")