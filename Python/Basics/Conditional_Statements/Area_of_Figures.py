figure = input()
if figure == "square":
    a = float(input())
    area = a**2
    print(f"{area:.3f}")
elif figure == "rectangle":
    a = float(input())
    b = float(input())
    area = a*b
    print(f"{area:.3f}")
elif figure == "circle":
    from math import pi
    r = float(input())
    area = pi * r**2
    print(f"{area:.3f}")
elif figure == "triangle":
    a = float(input())
    ha = float(input())
    area = a*ha/2
    print(f"{area:.3f}")
