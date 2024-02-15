# sequence = list(map(int, input().split(", ")))
# biggest_number = max(sequence)
# if biggest_number % 10 == 0:
#     biggest_group = biggest_number
# else:
#     biggest_group = (biggest_number // 10 + 1) * 10
# groups = [[] for group in range(10, biggest_group + 1, 10)]
# for number in sequence:
#     for group in range(1, len(groups) + 1):
#         if 0 <= group * 10 - number < 10:
#             groups[group - 1].append(number)
# for group in range(1, len(groups) + 1):
#     print(f"Group of {group * 10}'s: {groups[group - 1]}")
numbers = [int(number) for number in input().split(", ")]
current_group = 10
while numbers:
    filtered_numbers_for_current_group = [number for number in numbers if number <= current_group]
    print(f"Group of {current_group}'s: {filtered_numbers_for_current_group}")
    current_group += 10
    numbers = [number for number in numbers if number not in filtered_numbers_for_current_group]





