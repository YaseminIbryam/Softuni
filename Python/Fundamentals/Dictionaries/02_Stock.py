products_quantities = input().split()
stock_table = {}
for index in range(0, len(products_quantities), 2):
    product = products_quantities[index]
    quantity = int(products_quantities[index + 1])
    stock_table[product] = quantity
products_to_check = input().split()
for product in products_to_check:
    if product in stock_table.keys():
        print(f"We have {stock_table[product]} of {product} left")
    else:
        print(f"Sorry, we don't have {product}")