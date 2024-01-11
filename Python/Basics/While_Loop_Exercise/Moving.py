width = int(input())
length = int(input())
height = int(input())
apartment_size = width * length * height
is_space_finished = False
cartons = 0
command = input()
while command != "Done" and not is_space_finished:
    cartons += int(command)
    if cartons >= apartment_size:
        is_space_finished = True
        break
    command = input()

if is_space_finished:
    needed_cartons = cartons - apartment_size
    print(f"No more free space! You need {needed_cartons} Cubic meters more.")
else:
    cartons_left = apartment_size - cartons
    print(f"{cartons_left} Cubic meters left.")
