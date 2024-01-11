import math

number_days_without_Santa = int(input())
food_kg = int(input())
food_day_first_deer_kg = float(input())
food_day_second_deer_kg = float(input())
food_day_third_deer_kg = float(input())
food_per_day = food_day_first_deer_kg + food_day_second_deer_kg + food_day_third_deer_kg
need_food = food_per_day * number_days_without_Santa
if food_kg >= need_food:
    food_left = food_kg - need_food
    print(f"{math.floor(food_left)} kilos of food left.")
else:
    food_needed = need_food - food_kg
    print(f"{math.ceil(food_needed)} more kilos of food are needed.")