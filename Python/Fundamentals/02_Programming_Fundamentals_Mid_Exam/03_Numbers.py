numbers = list(map(int, input().split()))
average_value = sum(numbers) / len(numbers)
numbers.sort()
top_numbers = [number for number in numbers if number > average_value]
top_numbers.reverse()
if len(top_numbers) == 0:
    print("No")
elif len(top_numbers) <= 5:
    print(" ".join(list(map(str, top_numbers))))
else:
    output = [top_numbers[index] for index in range(5)]
    print(" ".join(list(map(str, output))))
