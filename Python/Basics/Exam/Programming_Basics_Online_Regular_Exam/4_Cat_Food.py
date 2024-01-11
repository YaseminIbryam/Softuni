number_cats = int(input())
small_cats = 0
big_cats = 0
huge_cats = 0
food_per_day_g = 0
for cat in range(number_cats):
    g_food = float(input())
    if 100 <= g_food < 200:
        small_cats += 1
    elif 200 <= g_food < 300:
        big_cats += 1
    elif 300 <= g_food < 400:
        huge_cats += 1
    food_per_day_g += g_food
food_kg = food_per_day_g/1000
price_food_per_day = food_kg * 12.45
print(f"Group 1: {small_cats} cats.")
print(f"Group 2: {big_cats} cats.")
print(f"Group 3: {huge_cats} cats.")
print(f"Price for food per day: {price_food_per_day:.2f} lv.")
