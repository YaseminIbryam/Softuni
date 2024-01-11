euro_to_bgn = 1.94
price_kg_vegetables = float(input())
price_kg_fruits = float(input())
kg_vegetables = int(input())
kg_fruits = int(input())
price_lv = price_kg_vegetables * kg_vegetables + price_kg_fruits * kg_fruits
price_euro = price_lv / euro_to_bgn
print(f"{price_euro:.2f}")
