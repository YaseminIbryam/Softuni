def factorial(number):
    factorial_of_num = 1
    for num in range(1, number + 1):
        factorial_of_num *= num
    return factorial_of_num


print(f"{factorial(int(input()))/factorial(int(input())):.2f}")
