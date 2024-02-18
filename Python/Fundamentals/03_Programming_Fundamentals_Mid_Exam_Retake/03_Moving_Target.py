sequence = list(map(int, input().split()))
while True:
    command = input()
    if command == "End":
        print("|".join(list(map(str, sequence))))
        break
    command_list = command.split()
    command = command_list[0]
    index = int(command_list[1])
    if command == "Shoot":
        if index >= len(sequence) or index < 0:
            continue
        power = int(command_list[2])
        sequence[index] -= power
        if sequence[index] <= 0:
            sequence.pop(index)
            # shot
    elif command == "Add":
        if index >= len(sequence) or index < 0:
            print("Invalid placement!")
            continue
        value = int(command_list[2])
        sequence.insert(index, value)
    elif command == "Strike":
        radius = int(command_list[2])
        indexes = list(range(index - radius, index + radius + 1))
        strike_missed = False
        for index in indexes:
            if index >= len(sequence) or index < 0:
                strike_missed = True
                break
        if strike_missed:
            print("Strike missed!")
            continue
        else:
            sequence = [target for index, target in enumerate(sequence) if index not in indexes]
