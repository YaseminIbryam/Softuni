sequence = list(map(int, input().split()))
removed_elements = []
while sequence:
    index = input()
    index = int(index)
    if index < 0:
        value = sequence[0]
        sequence[0] = sequence[-1]
    elif index >= len(sequence):
        value = sequence[-1]
        sequence[-1] = sequence[0]
    else:
        value = sequence.pop(index)
    removed_elements.append(value)
    sequence = [sequence[index] - value if sequence[index] > value
                else sequence[index] + value for index in range(len(sequence))]
print(sum(removed_elements))