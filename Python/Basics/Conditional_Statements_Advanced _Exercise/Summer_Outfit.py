degrees = int(input())
time = input()
Outfit = ""
Shoes = ""
if time == "Morning":
    if 10 <= degrees <= 18:
        Outfit = "Sweatshirt"
        Shoes = "Sneakers"
    elif 18 < degrees <= 24:
        Outfit = "Shirt"
        Shoes = "Moccasins"
    elif degrees >= 25:
        Outfit = "T-Shirt"
        Shoes = "Sandals"
elif time == "Afternoon":
    if 10 <= degrees <= 18:
        Outfit = "Shirt"
        Shoes = "Moccasins"
    elif 18 < degrees <= 24:
        Outfit = "T-Shirt"
        Shoes = "Sandals"
    elif degrees >= 25:
        Outfit = "Swim Suit"
        Shoes = "Barefoot"
elif time == "Evening":
    if 10 <= degrees <= 18:
        Outfit = "Shirt"
        Shoes = "Moccasins"
    elif 18 < degrees <= 24:
        Outfit = "Shirt"
        Shoes = "Moccasins"
    elif degrees >= 25:
        Outfit = "Shirt"
        Shoes = "Moccasins"
print(f"It's {degrees} degrees, get your {Outfit} and {Shoes}.")



