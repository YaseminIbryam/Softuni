quantity = int(input())
days = int(input())
budget = 0
totalSpirit = 0
price_ornament_set = 2
price_tree_skirt = 5
price_tree_garland = 3
price_tree_lights = 15
points_ornament_set = 5
points_tree_skirt = 3
points_tree_garland = 10
points_tree_lights = 17
for day in range(1, days + 1):
    if day % 11 == 0:
        quantity += 2
    if day % 2 == 0:
        budget += price_ornament_set * quantity
        totalSpirit += points_ornament_set
    if day % 3 == 0:
        budget += (price_tree_skirt + price_tree_garland) * quantity
        totalSpirit += points_tree_skirt + points_tree_garland
    if day % 5 == 0:
        budget += price_tree_lights * quantity
        totalSpirit += points_tree_lights
        if day % 3 == 0:
            totalSpirit += 30
    if day % 10 == 0:
        budget += price_tree_lights + price_tree_skirt + price_tree_garland
        totalSpirit -= 20
        if day == days:
            totalSpirit -= 30
print(f"Total cost: {budget}")
print(f"Total spirit: {totalSpirit}")
