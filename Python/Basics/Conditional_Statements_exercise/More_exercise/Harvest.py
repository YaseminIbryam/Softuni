import math
square_meters_of_vineyard = int(input())
grapes_for_square_meter = float(input())
needed_litres_wine = int(input())
number_of_workers = int(input())
square_meters_of_vineyard_for_wine = square_meters_of_vineyard * 40/100
kg_grapes = square_meters_of_vineyard_for_wine * grapes_for_square_meter
litres_wine = kg_grapes / 2.5
if litres_wine < needed_litres_wine:
    more_needed_wine = needed_litres_wine - litres_wine
    print(f"It will be a tough winter! More {math.floor(more_needed_wine)} liters wine needed.")
elif litres_wine >= needed_litres_wine:
    left_liters_wine = litres_wine - needed_litres_wine
    liters_per_person = left_liters_wine / number_of_workers
    print(f"Good harvest this year! Total wine: {math.floor(litres_wine)} liters.")
    print(f"{math.ceil(left_liters_wine)} liters left -> {math.ceil(liters_per_person)} liters per person.")
