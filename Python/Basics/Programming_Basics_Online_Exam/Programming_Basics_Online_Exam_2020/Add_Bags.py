price_bags_over_20kg = float(input())
kg_bags = float(input())
days_to_travel = int(input())
number_of_bags = int(input())
price = 0
price_of_bag = 0
if kg_bags < 10:
    price = 20 / 100 * price_bags_over_20kg
elif 10 <= kg_bags <= 20:
    price = 50 / 100 * price_bags_over_20kg
elif kg_bags > 20:
    price = price_bags_over_20kg
if days_to_travel > 30:
    price_of_bag = price * 10 / 100 + price
elif 7 <= days_to_travel <= 30:
    price_of_bag = price * 15 / 100 + price
elif days_to_travel < 7:
    price_of_bag = price * 40 / 100 + price
price_of_bags = price_of_bag * number_of_bags
print(f"The total price of bags is: {price_of_bags:.2f} lv.")
