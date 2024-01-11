budget = float(input())
number_nights = int(input())
price_per_night = float(input())
percent_extra_expenses = int(input())
if number_nights > 7:
    price_per_night *= (1-5/100)
price_all_nights = number_nights * price_per_night
extra_expenses = percent_extra_expenses/100 * budget
cost = price_all_nights + extra_expenses
if budget >= cost:
    left_money = budget - cost
    print(f"Ivanovi will be left with {left_money:.2f} leva after vacation.")
else:
    needed_money = cost - budget
    print(f"{needed_money:.2f} leva needed.")
