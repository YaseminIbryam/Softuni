collection_of_items = input().split("|")
budget = float(input())
prices = []
new_prices = []
for item in collection_of_items:
    item_list = item.split("->")
    type_item = item_list[0]
    price = float(item_list[1])
    if type_item == "Clothes" and price <= 50 \
            or type_item == "Shoes" and price <= 35\
            or type_item == "Accessories" and price <= 20.5:
        if budget >= price:
            budget -= price
            new_price = 1.4 * price
            prices.append(price)
            new_prices.append(new_price)

profit = sum(new_prices) - sum(prices)
budget = budget + sum(new_prices)
for new_price in new_prices:
    print(f"{new_price:.2f}", end=" ")
print(f"\nProfit: {profit:.2f}")
if budget >= 150:
    print("Hello, France!")
else:
    print("Not enough money.")


# ticket_price = 150
# collection_of_items = input().split("|")
# budget = float(input())
#
# new_prices = []
# profit = 0
#
# for item in collection_of_items:
#     type_item, price = [float(x) if x[-1].isdigit() else x for x in item.split("->")]
#
#     if budget >= price:
#         if any(type_item == product and price <= product_price
#                for product, product_price in (("Clothes", 50),
#                                               ("Shoes", 35),
#                                               ("Accessories", 20.5))):
#             budget -= price
#             new_price = price * 1.4
#             new_prices.append(new_price)
#             profit += new_prices[-1] - price
#
#
# print(" ".join(f"{x:.2f}" for x in new_prices))
# print(f"Profit: {profit:.2f}")
# print("Hello, France!" if budget + sum(new_prices) >= ticket_price else "Not enough money.")