def calculator(operator, number1, number2):
    if operator == "multiply":
        return number1 * number2
    elif operator == "divide":
        return number1 // number2
    elif operator == "add":
        return number1 + number2
    elif operator == "subtract":
        return number1 - number2


operator = input()
number1 = int(input())
number2 = int(input())
print(calculator(operator, number1, number2))
