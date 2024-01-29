employees_efficiency = int(input()) + int(input()) + int(input())
students = int(input())
hours = 0
while students > 0:
    hours += 1
    if hours % 4 == 0:
        continue
    students -= employees_efficiency
print(f"Time needed: {hours}h.")

