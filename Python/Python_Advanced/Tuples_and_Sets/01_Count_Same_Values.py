numbers = input().split()
numbers_count = {}
for number in numbers:
    numbers_count[float(number)] = numbers.count(number)
for number, count in numbers_count.items():
    print(f"{number} - {count} times")