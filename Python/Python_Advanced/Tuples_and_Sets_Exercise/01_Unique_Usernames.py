N = int(input())
names = {input() for _ in range(N)}
while names:
    print(names.pop())
    