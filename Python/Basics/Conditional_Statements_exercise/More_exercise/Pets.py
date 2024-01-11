import math

days = int(input())
food_kg = int(input())
food_per_day_for_dog_kg = float(input())
food_per_day_for_cat_kg = float(input())
food_per_day_for_turtle_g = float(input())
food_needed_kg = (food_per_day_for_cat_kg + food_per_day_for_dog_kg + food_per_day_for_turtle_g/1000) * days
if food_kg >= food_needed_kg:
    food_left = food_kg - food_needed_kg
    print(f"{math.floor(food_left)} kilos of food left.")
else:
    more_food_needed = food_needed_kg - food_kg
    print(f"{math.ceil(more_food_needed)} more kilos of food are needed.")
