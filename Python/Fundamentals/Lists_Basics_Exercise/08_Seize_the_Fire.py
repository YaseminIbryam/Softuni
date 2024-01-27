fire_level = input().split('#')
amount_of_water = int(input())
effort = 0
cells_put_out = []
for fire in fire_level:
    list_for_fire = fire.split(" = ")
    type_of_fire = list_for_fire[0]
    value_of_cell = int(list_for_fire[1])
    if type_of_fire == "High" and value_of_cell in range(81, 126)\
        or type_of_fire == "Medium" and value_of_cell in range(51, 81)\
            or type_of_fire == "Low" and value_of_cell in range(1, 51):
        if value_of_cell <= amount_of_water:
            amount_of_water -= value_of_cell
            cells_put_out.append(value_of_cell)
            effort += 0.25 * value_of_cell
total_fire = sum(cells_put_out)
print("Cells:")
for cell in cells_put_out:
    print(f" - {cell}")
print(f"Effort: {effort:.2f}")
print(f"Total Fire: {total_fire}")

