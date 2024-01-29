numbers = list(map(int, input().split(", ")))

for number in numbers:
    numbers.append(numbers.pop(numbers.index(0)))

print(numbers)
