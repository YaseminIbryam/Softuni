number = int(input())
position = int(input())
remainders = []
binary_number = 0
while number != 0:
    remainders.append(number % 2)
    number = number // 2
remainders[position] = 0
for index, digit in enumerate(remainders):
    binary_number += digit * (2**(len(remainders) - index - 1))
print(binary_number) 