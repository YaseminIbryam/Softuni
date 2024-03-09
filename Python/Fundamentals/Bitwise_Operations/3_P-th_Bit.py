number = int(input())
position = int(input())
remainders = []
while number != 0:
    remainders.append(number % 2)
    number = number // 2
try:
    print(remainders[position])
except IndexError:
    print(0)