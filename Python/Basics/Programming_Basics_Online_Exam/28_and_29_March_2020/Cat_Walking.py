minutes_walk_per_day = int(input())
number_of_walk_per_day = int(input())
calories_per_day = int(input())
burned_calories = 5 * minutes_walk_per_day * number_of_walk_per_day
if burned_calories >= calories_per_day / 2:
    print(f"Yes, the walk for your cat is enough. Burned calories per day: {burned_calories}.")
else:
    print(f"No, the walk for your cat is not enough. Burned calories per day: {burned_calories}.")