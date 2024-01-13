year = int(input())
next_year = year + 1
while True:
    digits = []
    unique_digits = []
    for digit in str(next_year):
        digits.append((int(digit)))
    unique_digits = list(set(digits))
    if len(digits) == len(unique_digits):
        break
    next_year += 1

print(next_year)
