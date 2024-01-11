number_of_orders = int(input())
total_price = 0
for order in range(number_of_orders):
    price_per_capsule = float(input())
    days = int(input())
    capsules_needed_per_day = int(input())
    if (price_per_capsule < 0.01 or price_per_capsule > 100.00
            or days < 1 or days > 31
            or capsules_needed_per_day < 1 or capsules_needed_per_day > 2000):
        continue
    price = price_per_capsule * capsules_needed_per_day * days
    print(f"The price for the coffee is: ${price:.2f}")
    total_price += price
print(f"Total: ${total_price:.2f}")


