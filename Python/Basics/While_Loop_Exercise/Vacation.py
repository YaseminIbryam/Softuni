money_for_vacation = float(input())
current_money = float(input())
days_money_spent = 0
days = 0
is_saved = True
while money_for_vacation > current_money:
    action = input()
    the_sum = float(input())
    days += 1
    if action == "spend":
        days_money_spent += 1
        current_money -= the_sum
        if current_money < 0:
            current_money = 0
        if days_money_spent == 5:
            is_saved = False
            break
    elif action == "save":
        current_money += the_sum
        days_money_spent = 0
if is_saved:
    print(f"You saved the money for {days} days.")
else:
    print("You can't save the money.")
    print(f"{days}")


