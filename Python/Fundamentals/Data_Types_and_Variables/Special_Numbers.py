n = int(input())
for number in range(1, n + 1):
    is_special = False
    sum_of_digits = 0
    for digit in str(number):
        sum_of_digits += int(digit)
    if sum_of_digits == 5 or sum_of_digits == 7 or sum_of_digits == 11:
        is_special = True
    print(f"{number} -> {is_special}")
