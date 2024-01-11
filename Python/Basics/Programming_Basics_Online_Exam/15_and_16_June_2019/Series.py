budget = float(input())
number_series = int(input())
cost = 0
for series in range(number_series):
    name_series = input()
    price = float(input())
    if name_series == "Thrones":
        price *= 0.5
    elif name_series == "Lucifer":
        price *= 0.6
    elif name_series == "Protector":
        price *= 0.7
    elif name_series == "TotalDrama":
        price *= 0.8
    elif name_series == "Area":
        price *= 0.9
    cost += price
if budget >= cost:
    left_money = budget - cost
    print(f"You bought all the series and left with {left_money:.2f} lv.")
else:
    needed_money = cost - budget
    print(f"You need {needed_money:.2f} lv. more to buy the series!")