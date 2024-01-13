budget = float(input())
price_1kg_flour = float(input())
price_1pack_eggs = price_1kg_flour * 0.75
price_1L_milk = price_1kg_flour * 1.25
price_250ml_milk = price_1L_milk / 4
price_all_products = price_1kg_flour + price_250ml_milk + price_1pack_eggs
current_bread = 0
colored_eggs = 0
counter_losing_eggs = 0
while budget >= price_all_products:
    budget -= price_all_products
    current_bread += 1
    colored_eggs += 3
    counter_losing_eggs += 1
    if counter_losing_eggs == 3:
        counter_losing_eggs = 0
        colored_eggs -= current_bread - 2
print(f"You made {current_bread} loaves of Easter bread! Now you have {colored_eggs} eggs and {budget:.2f}BGN left.")
