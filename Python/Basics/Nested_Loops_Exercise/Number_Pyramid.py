
n = int(input())
number_per_line = 1
no_number_in_line = 1
for number in range(1, n + 1):
    if number_per_line == no_number_in_line:
        print(number)
        number_per_line += 1
        no_number_in_line = 1
    else:
        print(number, end=" ")
        no_number_in_line += 1
#
#
# n = int(input())
# current = 1
# is_current_bigger_than_n = False
# for row in range(1, n + 1):
#     for col in range(1, row + 1):
#
#         if current > n:
#             is_current_bigger_than_n = True
#             break
#         print(str(current) + ' ', end='')
#         current += 1
#     if is_current_bigger_than_n:
#         break
#     print()
