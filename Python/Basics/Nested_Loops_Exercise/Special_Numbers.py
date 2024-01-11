# main_number = int(input())
# for number in range(1111, 10000):
#     special_digit_counter = 0
#     str_number = str(number)
#     for index, digit in enumerate(str_number):
#         if int(digit) == 0:
#             break
#         if main_number % int(digit) == 0:
#             special_digit_counter += 1
#         if special_digit_counter == 4:
#             print(number, end=" ")

main_number = int(input())
for number in range(1111, 10000):
    special_digit_counter = 0
    str_number = str(number)
    if int(str_number[0]) != 0 \
            and int(str_number[1]) != 0 \
            and int(str_number[2]) != 0 \
            and int(str_number[3]) != 0:
        if main_number % int(str_number[0]) == 0 \
                and main_number % int(str_number[1]) == 0 \
                and main_number % int(str_number[2]) == 0 \
                and main_number % int(str_number[3]) == 0:
            print(number, end=" ")
