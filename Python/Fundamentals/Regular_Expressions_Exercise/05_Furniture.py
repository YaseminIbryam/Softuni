import re

pattern = r'>>([a-zA-Z]+)<<([0-9]+\.?[0-9]*)!(\d+\b)'
bought_furniture = []
total_price = 0
while True:
    purchase = input()
    if purchase == "Purchase":
        break
    match = re.search(pattern, purchase)
    if match:
        furniture, price, quantity = match.groups()
        bought_furniture.append(furniture)
        total_price += float(price) * int(quantity)
print("Bought furniture:")
for furniture in bought_furniture:
    print(furniture)
print(f"Total money spend: {total_price:.2f}")



