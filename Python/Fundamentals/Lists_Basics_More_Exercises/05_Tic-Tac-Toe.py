first_line = input().split()
second_line = input().split()
third_line = input().split()
all_lines = [first_line, second_line, third_line]


def check_winner():
    if number == "1":
        print("First player won")
    elif number == "2":
        print("Second player won")
    else:
        print("Draw!")
    quit()


for index in range(3):
    if first_line[index] == second_line[index] == third_line[index]:
        number = first_line[index]
        check_winner()
for line in all_lines:
    if line[0] == line[1] == line[2]:
        number = line[0]
        check_winner()
if first_line[0] == second_line[1] == third_line[2]:
    number = first_line[0]
    check_winner()
if first_line[2] == second_line[1] == third_line[0]:
    number = first_line[2]
    check_winner()
