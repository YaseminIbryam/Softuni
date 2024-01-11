number_days = int(input())
money = 0
won_days = 0
lost_days = 0
for day in range(number_days):
    command = input()
    money_day = 0
    won_games = 0
    lost_games = 0
    while command != "Finish":
        name_game = command
        result = input()
        if result == "win":
            money_day += 20
            won_games += 1
        elif result == "lose":
            lost_games += 1
        command = input()
    if won_games > lost_games:
        won_days += 1
        money_day *= (1+10/100)
    else:
        lost_days += 1
    money += money_day
if won_days > lost_days:
    money *= (1+20/100)
    print(f"You won the tournament! Total raised money: {money:.2f}")
else:
    print(f"You lost the tournament! Total raised money: {money:.2f}")
