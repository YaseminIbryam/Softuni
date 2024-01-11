from sys import maxsize

command = input()
most_goals = -maxsize
best_player = ""
while command != "END":
    name_player = command
    number_goals = int(input())
    if number_goals > most_goals:
        most_goals = number_goals
        best_player = name_player
    if number_goals >= 10:
        break
    command = input()
print(f"{best_player} is the best player!")
if most_goals >= 3:
    print(f"He has scored {most_goals} goals and made a hat-trick !!!")
else:
    print(f"He has scored {most_goals} goals.")

