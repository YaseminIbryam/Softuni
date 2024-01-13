first_string = input()
second_string = input()
last_printed_string = first_string
for index in range(len(first_string)):
    current_string = second_string[:index + 1] + first_string[index + 1:]
    if last_printed_string != current_string:
        print(current_string)
    last_printed_string = current_string
