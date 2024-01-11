number_floor = int(input())
number_rooms_per_floor = int(input())
for rooms in range(number_rooms_per_floor):
    if rooms != number_rooms_per_floor - 1:
        print(f"L{number_floor}{rooms}", end=" ")
    else:
        print(f"L{number_floor}{rooms}")
for floors in range(number_floor - 1, 0, -1):
    for rooms in range(number_rooms_per_floor):
        if floors % 2 == 0:
            room_type = "O"
        else:
            room_type = "A"
        if rooms == number_rooms_per_floor - 1:
            print(f"{room_type}{floors}{rooms}")
        else:
            print(f"{room_type}{floors}{rooms}", end=" ")
