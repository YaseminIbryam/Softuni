width = float(input())
length = float(input())
height = float(input())
average_height_astronauts = float(input())
volume = width * length * height
room_per_astronaut = 2 * 2 * (average_height_astronauts + 0.4)
number_astronauts = int(volume//room_per_astronaut)
if 3 <= number_astronauts <= 10:
    print(f"The spacecraft holds {number_astronauts} astronauts.")
elif 3 > number_astronauts:
    print("The spacecraft is too small.")
elif number_astronauts > 10:
    print("The spacecraft is too big.")

