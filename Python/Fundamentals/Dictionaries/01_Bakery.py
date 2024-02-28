food_quantities = input().split()
stock_dict = {}
for index in range(0, len(food_quantities), 2):
    food = food_quantities[index]
    quantity = int(food_quantities[index + 1])
    stock_dict[food] = quantity
print(stock_dict)
