budget = int(input())
season = input()
number_of_fishermen = int(input())
boat_rent = 0
discount = 0
extra_discount = 0
if season == "Spring":
    boat_rent = 3000
elif season == "Winter":
    boat_rent = 2600
else:
    boat_rent = 4200
if number_of_fishermen <= 6:
    discount = 10/100
elif 7 < number_of_fishermen <= 11:
    discount = 15/100
elif number_of_fishermen >= 12:
    discount = 25/100
if number_of_fishermen % 2 == 0 and not season == "Autumn":
    extra_discount = 5/100
total_cost = (boat_rent * (1 - discount)) * (1 - extra_discount)
if total_cost > budget:
    needed_money = total_cost - budget
    print(f"Not enough money! You need {needed_money:.2f} leva.")
else:
    left_money = budget - total_cost
    print(f"Yes! You have {left_money:.2f} leva left.")

