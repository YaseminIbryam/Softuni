def tribonacci_sequence(number):
    sequence = []
    for num in range(number):
        if num == 0 or num == 1:
            sequence.append(1)
        elif num == 2:
            sequence.append(2)
        else:
            sequence.append(sequence[num-2] + sequence[num-1] + sequence[num-3])
    return " ".join(list(map(str,sequence)))


print(tribonacci_sequence(int(input())))