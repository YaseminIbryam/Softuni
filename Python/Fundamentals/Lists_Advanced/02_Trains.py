train = [0 for number in range(int(input()))]
command = input().split()
while command[0] != "End":
    command_action = command[0]
    if command_action == "add":
        people = int(command[1])
        train[-1] += people
    elif command_action == "insert":
        index = int(command[1])
        people = int(command[2])
        train[index] += people
    elif command_action == "leave":
        index = int(command[1])
        people = int(command[2])
        train[index] -= people
    command = input().split()
print(train)