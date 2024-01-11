Lily_age = int(input())
price_washing_machine = float(input())
price_for_toy = int(input())
saved_money = 0
toys = 0
for ages in range(1, Lily_age + 1):
    if ages % 2 == 0:
        saved_money += ages * 5
        saved_money -= 1
    else:
        toys += 1
saved_money = saved_money + toys * price_for_toy
if saved_money >= price_washing_machine:
    left_money = saved_money - price_washing_machine
    print(f"Yes! {left_money:.2f}")
else:
    money_needed = price_washing_machine - saved_money
    print(f"No! {money_needed:.2f}")



