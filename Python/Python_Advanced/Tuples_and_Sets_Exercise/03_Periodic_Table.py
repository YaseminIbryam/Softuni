n = int(input())
elements = set()
for _ in range(n):
    line = set(input().split())
    elements.update(line)
while elements:
    print(elements.pop())
