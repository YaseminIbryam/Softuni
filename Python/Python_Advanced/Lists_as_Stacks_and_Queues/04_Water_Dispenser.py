from collections import deque

quantity = int(input())
name = input()
queue = deque()
while name != 'Start':
    queue.append(name)
    name = input()

command = input().split()
while command[0] != 'End':
    if command[0] == 'refill':
        quantity += int(command[1])
    else:
        name = queue.popleft()
        if quantity >= int(command[0]):
            quantity -= int(command[0])
            print(f"{name} got water")
        else:
            print(f"{name} must wait")
    command = input().split()
print(f"{quantity} liters left")
