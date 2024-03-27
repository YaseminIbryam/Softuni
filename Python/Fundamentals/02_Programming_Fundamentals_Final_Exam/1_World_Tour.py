def is_index_valid(index):
    if 0 <= index <= len(initial_string):
        return True
    return False


def add_stop(index: int, string: str):
    if is_index_valid(index):
        return initial_string[:index] + string + initial_string[index:]
    return initial_string


def remove_stop(start_index: int, end_index: int):
    if is_index_valid(start_index) and is_index_valid(end_index + 1):
        return initial_string[:start_index] + initial_string[end_index + 1:]
    return initial_string


def switch(old_string, new_string):
    if old_string in initial_string:
        return initial_string.replace(old_string, new_string)
    return initial_string

initial_string = input()
while True:
    command_list = input()
    if command_list == 'Travel':
        break
    command_list = command_list.split(':')
    command = command_list[0]
    if command == 'Add Stop':
        initial_string = add_stop(int(command_list[1]), command_list[2])
    elif command == 'Remove Stop':
        initial_string = remove_stop(int(command_list[1]), int(command_list[2]))
    elif command == 'Switch':
        initial_string = switch(command_list[1], command_list[2])
    print(initial_string)
print(f"Ready for world tour! Planned stops: {initial_string}")
