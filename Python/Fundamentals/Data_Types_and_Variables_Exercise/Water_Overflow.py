n = int(input())
liters_tank = 0
capacity = 255
for line in range(n):
    liters_of_water = int(input())
    if capacity >= liters_of_water:
        liters_tank += liters_of_water
        capacity -= liters_of_water
    else:
        print("Insufficient capacity!")
print(liters_tank)

