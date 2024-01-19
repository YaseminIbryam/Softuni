from math import ceil

number = int(input())
is_prime = True
for i in range(2, ceil(number ** 0.5)):
    if number % i == 0:
        is_prime = False
        break
print(is_prime)
