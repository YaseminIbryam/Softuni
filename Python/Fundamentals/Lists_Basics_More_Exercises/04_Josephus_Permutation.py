people_in_the_circle = list(map(int, input().split()))
k = int(input())
executions = []
index = k - 1
while len(people_in_the_circle) > 0:
    while index >= len(people_in_the_circle):
        index -= len(people_in_the_circle)
    executions.append(people_in_the_circle.pop(index))
    index += 2
print("[" + ",".join(map(str, executions)) + "]")