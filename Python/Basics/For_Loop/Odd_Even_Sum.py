count_numbers = int(input())
odd_sum = 0
even_sum = 0
for i in range(count_numbers):
    number = int(input())
    if i % 2 == 0:
        odd_sum += number
    else:
        even_sum += number

if odd_sum == even_sum:
    print(f"Yes\nSum = {odd_sum}")
else:
    difference = abs(odd_sum - even_sum)
    print(f"No\nDiff = {difference}")
