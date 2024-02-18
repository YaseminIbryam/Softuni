sequence = list(map(int, input().split()))
removed_elements = []
while True:
    index = input()
    if index == '':
        print(sum(removed_elements))
        break
    index = int(index)
    if index < 0:
        value = sequence[index]
        sequence[index] = sequence[-1]
    elif index >= len(sequence):
        value = sequence[-1]
        sequence[-1] = sequence[index]
    else:
        value = sequence.pop(index)
    removed_elements.append(value)
    sequence = [sequence[index] - value if sequence[index] > value
                else sequence[index] + value for index in range(len(sequence))]
