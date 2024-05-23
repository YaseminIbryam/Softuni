stack = []
lines = int(input())
for line in range(lines):
    query = input().split()
    command_number = query[0]
    if command_number == '1':
        stack.append(int(query[1]))
    elif command_number == '2':
        if stack:
            stack.pop()
    elif command_number == '3':
        if stack:
            print(max(stack))
    elif command_number == '4':
        if stack:
            print(min(stack))
while stack:
    print(stack.pop(), end='')
    if stack:
        print(', ', end='')
