inherited_money = float(input())
year_for_life = int(input())
age = 18
spent_money = 0
for year in range(1800, year_for_life + 1):
    if year % 2 == 0:
        spent_money += 12000
    else:
        spent_money += 12000 + 50 * age
    age += 1
if inherited_money >= spent_money:
    money_left = inherited_money - spent_money
    print(f"Yes! He will live a carefree life and will have {money_left:.2f} dollars left.")
else:
    money_needed = spent_money - inherited_money
    print(f"He will need {money_needed:.2f} dollars to survive.")
