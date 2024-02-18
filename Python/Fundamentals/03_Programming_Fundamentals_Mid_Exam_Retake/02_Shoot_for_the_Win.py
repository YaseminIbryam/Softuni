sequence = list(map(int, input().split()))
shot_targets = 0
while True:
    command = input()
    if command == "End":
        print(f"Shot targets: {shot_targets} -> {' '.join(list(map(str, sequence)))}")
        break
    index = int(command)
    if index >= len(sequence) or sequence[index] == -1:
        continue
    shot_targets += 1
    shot_value = sequence[index]
    sequence[index] = -1
    for index, target in enumerate(sequence):
        if target != -1:
            sequence[index] = (target + shot_value if target <= shot_value else target - shot_value)


