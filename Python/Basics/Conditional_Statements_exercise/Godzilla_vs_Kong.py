budget = float(input())
number_of_extras = float(input())
price_for_dress_for_extra = float(input())
decor = 10/100 * budget
if number_of_extras > 150:
    price_for_dress_for_extra = price_for_dress_for_extra - price_for_dress_for_extra * 10/100
expenses = price_for_dress_for_extra * number_of_extras + decor
if expenses > budget:
    print("Not enough money!")
    print(f"Wingard needs {(expenses - budget):.2f} leva more.")
elif expenses <= budget:
    print("Action!")
    print(f"Wingard starts filming with {(budget-expenses):.2f} leva left.")

