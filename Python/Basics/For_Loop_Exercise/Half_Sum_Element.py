from sys import maxsize

count_numbers = int(input())
sum_of_numbers = 0
max_num = -maxsize  # minsize
for _ in range(count_numbers):
    number = int(input())
    sum_of_numbers += number
    if number > max_num:
        max_num = number
if sum_of_numbers / 2 == max_num:
    print(f"Yes\nSum = {max_num}")
else:
    difference = abs(max_num - (sum_of_numbers - max_num))
    print(f"No\nDiff = {difference}")
