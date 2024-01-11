price_page = float(input())
price_cover = float(input())
discount_percent = int(input())
designer_cost = float(input())
percent_paid_by_team = int(input())
pages = 899
covers = 2
price_pages = pages * price_page
price_covers = covers * price_cover
price_paper = (price_pages + price_covers) * (1-discount_percent/100)
total_cost = price_paper + designer_cost
Avtonom_bill = total_cost * (1-percent_paid_by_team/100)
print(f"Avtonom should pay {Avtonom_bill:.2f} BGN.")
