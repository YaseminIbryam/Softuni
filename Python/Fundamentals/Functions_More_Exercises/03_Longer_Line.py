import math


def longer_line(point1, point2, point3, point4):
    line1 = math.sqrt((point1[0] - point2[0]) ** 2 + (point1[1] - point2[1]) ** 2)
    line2 = math.sqrt((point3[0] - point4[0]) ** 2 + (point3[1] - point4[1]) ** 2)
    if line1 > line2:
        return point1, point2
    else:
        return point3, point4


def which_is_close_to_center(point_1, point_2):
    distance_1 = math.sqrt(point_1[0] ** 2 + point_1[1] ** 2)
    distance_2 = math.sqrt(point_2[0] ** 2 + point_2[1] ** 2)
    if distance_1 > distance_2:
        point_1, point_2 = tuple(map(math.floor,point_2)), tuple(map(math.floor,point_1))
    else:
        point_1, point_2 = tuple(map(math.floor,point_1)), tuple(map(math.floor,point_2))
    return point_1, point_2


point1, point2, point3, point4 = (float(input()), float(input())), (float(input()), float(input())), (
    float(input()), float(input())), (float(input()), float(input()))

point1, point2 = longer_line(point1, point2, point3, point4)

point1, point2 = which_is_close_to_center(point1, point2)
print(point1, point2, sep="")
