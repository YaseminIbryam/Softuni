def insert_space(index: int):
    return concealed_message[:index] + ' ' + concealed_message[index:]


def reverse(substring: str):
    if substring in concealed_message:
        message = concealed_message.replace(substring, '', 1)
        message += substring[::-1]
        return message
    return 'error'



def change_all(substring: str, replacement: str):
    if substring in concealed_message:
        message = concealed_message.replace(substring, replacement)
        return message
    return concealed_message


concealed_message = input()
while True:
    command_list = input().split(':|:')
    if command_list[0] == 'Reveal':
        break
    command = command_list[0]
    if command == 'InsertSpace':
        concealed_message = insert_space(int(command_list[1]))
    elif command == 'Reverse':
        message = reverse(command_list[1])
        if message == 'error':
            print('error')
            continue
        concealed_message = message
    elif command == 'ChangeAll':
        concealed_message = change_all(command_list[1], command_list[2])
    print(concealed_message)
print(f"You have a new text message: {concealed_message}")