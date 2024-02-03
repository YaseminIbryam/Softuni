def is_perfect_number(number):
    divisors = [num for num in range(1, number) if number % num == 0]
    if sum(divisors) == number:
        return "We have a perfect number!"
    return "It's not so perfect."


print(is_perfect_number(int(input())))