def urgent(item, initial_list):
    if item not in initial_list:
        initial_list.insert(0, item)
    return initial_list


def unnecessary(item, initial_list):
    if item in initial_list:
        initial_list.remove(item)
    return initial_list


def correct(old_item, new_item, initial_list):
    if old_item in initial_list:
        initial_list[initial_list.index(old_item)] = new_item
    return initial_list


def rearrange(item, initial_list):
    if item in initial_list:
        initial_list.remove(item)
        initial_list.append(item)
    return initial_list


groceries_list = input().split('!')
while True:
    command = input()
    if command == "Go Shopping!":
        print(", ".join(groceries_list))
        break
    command_list = command.split()
    command = command_list[0]
    if command == "Urgent":
        groceries_list = urgent(command_list[1], groceries_list)
    elif command == "Unnecessary":
        groceries_list = unnecessary(command_list[1], groceries_list)
    elif command == "Correct":
        groceries_list = correct(command_list[1], command_list[2], groceries_list)
    elif command == "Rearrange":
        groceries_list = rearrange(command_list[1], groceries_list)


