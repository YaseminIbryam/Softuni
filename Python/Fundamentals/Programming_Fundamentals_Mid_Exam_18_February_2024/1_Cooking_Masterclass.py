from math import ceil
budget = float(input())
students = int(input())
price_package_flour = float(input())
price_egg = float(input())
price_apron = float(input())
eggs = 0
aprons = 0
flours = 0
for student in range(1, students + 1):
    eggs += 10
    aprons += 1
    flours += 1
    if student % 5 == 0:
        flours -= 1
aprons += ceil(aprons * 0.2)
total_price = price_apron * aprons + price_package_flour * flours + price_egg * eggs
if total_price <= budget:
    print(f"Items purchased for {total_price:.2f}$.")
else:
    needed_money = total_price - budget
    print(f"{needed_money:.2f}$ more needed.")
