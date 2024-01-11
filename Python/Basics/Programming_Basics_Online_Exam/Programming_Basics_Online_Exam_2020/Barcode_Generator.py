start = int(input())
end = int(input())
start_first_digit = int(str(start)[0])
start_second_digit = int(str(start)[1])
start_third_digit = int(str(start)[2])
start_fourth_digit = int(str(start)[3])
end_first_digit = int(str(end)[0])
end_second_digit = int(str(end)[1])
end_third_digit = int(str(end)[2])
end_fourth_digit = int(str(end)[3])
for number in range(start, end + 1):
    for index, digit in enumerate(str(number)):
        digit = int(digit)
        if index == 0:
            if start_first_digit > digit or end_first_digit < digit:
                break
        elif index == 1:
            if start_second_digit > digit or end_second_digit < digit:
                break
        elif index == 2:
            if start_third_digit > digit or end_third_digit < digit:
                break
        elif index == 3:
            if start_fourth_digit > digit or end_fourth_digit < digit:
                break
        if digit % 2 == 0:
            break
    else:
        print(number, end=" ")


