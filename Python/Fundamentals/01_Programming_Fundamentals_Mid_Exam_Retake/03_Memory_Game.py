sequence = input().split()
indexes = input()
moves = 0
while indexes != "end":
    moves += 1
    indexes = indexes.split()
    first_index = int(indexes[0])
    second_index = int(indexes[1])
    if len(sequence) == 0:
        print(f"You have won in {moves - 1} turns!")
        break
    elif first_index == second_index or first_index >= len(sequence) or second_index >= len(sequence) \
            or first_index < 0 or second_index < 0:
        print("Invalid input! Adding additional elements to the board")
        sequence.insert(len(sequence) // 2, f"-{moves}a")
        sequence.insert(len(sequence) // 2, f"-{moves}a")
    elif sequence[first_index] == sequence[second_index]:
        element = sequence[first_index]
        print(f"Congrats! You have found matching elements - {element}!")
        sequence.remove(element)
        sequence.remove(element)
    elif sequence[first_index] != sequence[second_index]:
        print("Try again!")
    indexes = input()
else:
    if len(sequence) == 0:
        print(f"You have won in {moves} turns!")
    else:
        print("Sorry you lose :(")
        print(" ".join(sequence))

