def calculate_total_price(product, quantity):
    if product == "coffee":
        total_price = quantity * 1.5
    elif product == "water":
        total_price = quantity * 1
    elif product == "coke":
        total_price = quantity * 1.4
    elif product == "snacks":
        total_price = quantity * 2
    return total_price


product = input()
quantity = int(input())
result = calculate_total_price(product, quantity)
print(f"{result:.2f}")
