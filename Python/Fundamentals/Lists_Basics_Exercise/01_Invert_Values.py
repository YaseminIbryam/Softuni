numbers = (list(map(int, input().split())))
opposite_numbers = []
for num in numbers:
    num = -num
    opposite_numbers.append(num)

print(opposite_numbers)
