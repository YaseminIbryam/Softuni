def letters(case: str):
    if case == "Upper":
        return username.upper()
    elif case == "Lower":
        return username.lower()


def reverse(start_index: int, end_index: int):
    if len(username) > start_index >= 0 and len(username) > end_index >= 0:
        print((username[start_index:end_index + 1])[::-1])


def substring(substring: str):
    if substring in username:
        name = username.replace(substring, '')
        print(name)
        return name
    else:
        print(f"The username {username} doesn't contain {substring}.")


def replace(char: str):
    name = username.replace(char, '-')
    print(name)
    return name


def is_valid(char: str):
    if char in username:
        print("Valid username.")
    else:
        print(f"{char} must be contained in your username.")



username = input()
while True:
    command = input().split()
    if command[0] == "Registration":
        break
    if command[0] == "Letters":
        username = letters(command[1])
        print(username)
    elif command[0] == "Reverse":
        reverse(int(command[1]), int(command[2]))
    elif command[0] == "Substring":
        name = substring(command[1])
        if name:
            username = name
    elif command[0] == "Replace":
        username = replace(command[1])
    elif command[0] == "IsValid":
        is_valid(command[1])