# number_of_lines = int(input())
# ascii_sum = 0
# for line in range(number_of_lines):
#     letter = input()
#     ascii_sum += ord(letter)
# print(f"The sum equals: {ascii_sum}")

print(f"The sum equals: {sum(ord(input()) for _ in range(int(input())))}")
