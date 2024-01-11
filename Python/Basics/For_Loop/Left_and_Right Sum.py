count_numbers = int(input())
left_sum = 0
right_sum = 0
for i in range(count_numbers * 2):
    number = int(input())
    if i < count_numbers:
        left_sum += number
    else:
        right_sum += number
if left_sum == right_sum:
    print(f"Yes, sum = {left_sum}")
else:
    difference = abs(left_sum - right_sum)
    print(f"No, diff = {difference}")
