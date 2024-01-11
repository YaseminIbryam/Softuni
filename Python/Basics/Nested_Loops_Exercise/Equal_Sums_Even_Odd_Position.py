# number_1 = int(input())
# number_2 = int(input())
# for number in range(number_1, number_2 + 1):
#     str_number = str(number)
#     if int(str_number[0]) + int(str_number[2]) + int(str_number[4]) ==\
#             int(str_number[1]) + int(str_number[3]) + int(str_number[5]):
#         print(number, end=" ")

number_1 = int(input())
number_2 = int(input())
for number in range(number_1, number_2 + 1):
    odd_sum = 0
    even_sum = 0
    str_number = str(number)
    for index, digit in enumerate(str_number):
        if index % 2 == 0:
            odd_sum += int(digit)
        else:
            even_sum += int(digit)
    if even_sum == odd_sum:
        print(number, end=" ")
