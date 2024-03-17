def add(piece, composer, key):
    if piece not in collection.keys():
        collection[piece] = {'composer': composer, 'key': key}
        print(f"{piece} by {composer} in {key} added to the collection!")
    else:
        print(f"{piece} is already in the collection!")


def remove(piece):
    if piece in collection:
        del collection[piece]
        print(f"Successfully removed {piece}!")
    else:
        print(f"Invalid operation! {piece} does not exist in the collection.")


def change_key(piece, new_key):
    if piece in collection.keys():
        collection[piece]['key'] = new_key
        print(f"Changed the key of {piece} to {new_key}!")
    else:
        print(f"Invalid operation! {piece} does not exist in the collection.")


pieces = int(input())
collection = {}
for piece_info in range(pieces):
    name, composer, key = input().split('|')
    collection[name] = {'composer': composer, 'key': key}
while True:
    command_info = input()
    if command_info == "Stop":
        break
    command_info = command_info.split('|')
    command = command_info[0]
    if command == "Add":
        add(command_info[1], command_info[2], command_info[3])
    elif command == "Remove":
        remove(command_info[1])
    elif command == "ChangeKey":
        change_key(command_info[1], command_info[2])
for piece_, composer_key in collection.items():
    print(f"{piece_} -> Composer: {composer_key['composer']}, Key: {composer_key['key']}")


