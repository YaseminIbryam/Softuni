parking = {}


def register(username, license_plate_number, dictionary):
    if username in parking.keys():
        message = f"ERROR: already registered with plate number {license_plate_number}"
    else:
        message = f"{username} registered {license_plate_number} successfully"
        dictionary[username] = license_plate_number
    return dictionary, message


def unregister(username, dictionary):
    if username in parking.keys():
        del dictionary[username]
        message = f"{username} unregistered successfully"
    else:
        message = f"ERROR: user {username} not found"
    return dictionary, message


for command in range(int(input())):
    command = input().split()
    if command[0] == "register":
        parking, message = register(command[1], command[2], parking)
    else:  # elif command[0] == "unregister":
        parking, message = unregister(command[1], parking)
    print(message)
for username, license_plate_number in parking.items():
    print(f"{username} => {license_plate_number}")
