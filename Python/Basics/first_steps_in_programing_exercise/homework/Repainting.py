protective_nylon = 1.50
paint = 14.50
paint_divider = 5.00
bag = 0.40
needed_nylon = int(input())
price_nylon = (needed_nylon + 2)*protective_nylon
needed_paint = int(input())
price_paint = (needed_paint + needed_paint * 0.1)*paint
needed_divider = int(input())
price_divider = needed_divider * paint_divider
master_per_hour = (price_paint + price_nylon + price_divider + bag)*0.3
hours = int(input())
master_price = master_per_hour * hours
bill = price_divider + price_paint + price_nylon + bag + master_price
print(bill)
