wanted_income = float(input())
command = input()
income = 0
while command != "Party!":
    name_cocktail = command
    number_cocktails_for_order = int(input())
    price_cocktail = len(name_cocktail)
    price_cocktails = number_cocktails_for_order * price_cocktail
    if price_cocktails % 2 != 0:
        price_cocktails *= (1-25/100)
    income += price_cocktails
    if income >= wanted_income:
        print("Target acquired.")
        break
    command = input()

if command == "Party!":
    needed_sum = wanted_income - income
    print(f"We need {needed_sum:.2f} leva more.")

print(f"Club income - {income:.2f} leva.")