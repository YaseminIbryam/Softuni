start_interval = int(input())
finish_interval = int(input())
magic_number = int(input())
is_combination_available = False
number_of_combination = 0
is_done = False
for number1 in range(start_interval, finish_interval + 1):
    if is_done:
        break
    for number2 in range(start_interval, finish_interval + 1):
        number_of_combination += 1
        if number1 + number2 == magic_number:
            print(f"Combination N:{number_of_combination} ({number1} + {number2} = {magic_number})")
            is_combination_available = True
            is_done = True
if not is_combination_available:
    print(f"{number_of_combination} combinations - neither equals {magic_number}")
