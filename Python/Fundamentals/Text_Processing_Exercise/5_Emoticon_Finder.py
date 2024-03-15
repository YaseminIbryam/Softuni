message = input()
for index, char in enumerate(message):
    if char == ':':
        print(f':{message[index + 1]}')
