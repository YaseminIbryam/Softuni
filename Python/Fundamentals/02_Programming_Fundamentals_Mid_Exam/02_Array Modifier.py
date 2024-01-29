values = list(map(int, input().split()))
command = input().split()
while command[0] != "end":
    if command[0] == "swap":
        index1 = int(command[1])
        index2 = int(command[2])
        values[index1], values[index2] = values[index2], values[index1]
    elif command[0] == "multiply":
        index1 = int(command[1])
        index2 = int(command[2])
        values[index1] *= values[index2]
    elif command[0] == "decrease":
        values = [element - 1 for element in values]
    command = input().split()
print((", ".join(list(map(str, values)))))
