def move(number: int, message: str):
    letters = message[:number]
    replaced_letters = []
    for letter in letters:
        if letter not in replaced_letters:
            count = letters.count(letter)
            message = message.replace(letter, '', count)
            replaced_letters.append(letter)
    message += letters
    return message


def insert(index: int, value: str, message: str):
    left_side = message[:index]
    right_side = message[index:]
    message = left_side + value + right_side
    return message


def change_all(substring: str, replacement: str, message: str):
    message = message.replace(substring, replacement)
    return message


encrypted_message = input()
while True:
    instructions = input()
    if instructions == "Decode":
        break
    instructions = instructions.split("|")
    command = instructions[0]
    if command == "Move":
        encrypted_message = move(int(instructions[1]), encrypted_message)
    elif command == "Insert":
        encrypted_message = insert(int(instructions[1]), instructions[2], encrypted_message)
    elif command == "ChangeAll":
        encrypted_message = change_all(instructions[1], instructions[2], encrypted_message)
print("The decrypted message is:", encrypted_message)