type_drink = input()
sugar = input()
number_drinks = int(input())
price_per_drink = 0
if type_drink == "Espresso":
    if sugar == "Without":
        price_per_drink = 0.90
    elif sugar == "Normal":
        price_per_drink = 1
    elif sugar == "Extra":
        price_per_drink = 1.20
elif type_drink == "Cappuccino":
    if sugar == "Without":
        price_per_drink = 1
    elif sugar == "Normal":
        price_per_drink = 1.20
    elif sugar == "Extra":
        price_per_drink = 1.60
elif type_drink == "Tea":
    if sugar == "Without":
        price_per_drink = 0.50
    elif sugar == "Normal":
        price_per_drink = 0.60
    elif sugar == "Extra":
        price_per_drink = 0.70
if sugar == "Without":
    price_per_drink *= (1-35/100)
if type_drink == "Espresso" and number_drinks >= 5:
    price_per_drink *= (1-25/100)
bill = price_per_drink * number_drinks
if bill > 15:
    bill *= (1-20/100)
print(f"You bought {number_drinks} cups of {type_drink} for {bill:.2f} lv.")
