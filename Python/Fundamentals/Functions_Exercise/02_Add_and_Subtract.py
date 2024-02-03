def sum_numbers(number1, number2):
    number1 + number2
    return number1 + number2


def subtract(sum_of_first_two, number3):
    return sum_of_first_two - number3


def add_and_subtract():
    number1 = int(input())
    number2 = int(input())
    number3 = int(input())
    sum_of_first_two = sum_numbers(number1, number2)
    result = subtract(sum_of_first_two, number3)
    return result


print(add_and_subtract())
