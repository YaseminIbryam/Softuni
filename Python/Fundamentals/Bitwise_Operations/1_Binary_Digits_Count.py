number = int(input())
binary_digit = int(input())
remainders = []
while number != 0:
    remainders.append(number % 2)
    number = number // 2
count_of_digit = remainders.count(binary_digit)
print(count_of_digit)
