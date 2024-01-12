year = int(input())
is_happy_year = False
while not is_happy_year:
    digits = []
    unique_digits = []
    for digit in str(year):
        digits.append((int(digit)))
    unique_digits = list(set(digits))
    if len(digits) == len(unique_digits):
        is_happy_year = True
        break
    year += 1
print(year)