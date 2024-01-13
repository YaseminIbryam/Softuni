number = int(input())
digits = []
for digit in str(number):
    digits.append(int(digit))
digits.sort()
digits.reverse()
print(*digits, sep='')
