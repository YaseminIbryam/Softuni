import math


def which_is_close_to_center(point_1, point_2):
    distance_1 = math.sqrt(point_1[0] ** 2 + point_1[1] ** 2)
    distance_2 = math.sqrt(point_2[0] ** 2 + point_2[1] ** 2)
    if distance_1 <= distance_2:
        return tuple(map(math.floor,point_1))
    else:
        return tuple(map(math.floor, point_2))


point_1 = (float(input()), float(input()))
point_2 = (float(input()), float(input()))

print(which_is_close_to_center(point_1, point_2))
