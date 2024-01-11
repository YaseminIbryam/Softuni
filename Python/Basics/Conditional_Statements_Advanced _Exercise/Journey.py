budget = float(input())
season = input()
cost = 0
stay = ""
if budget <= 100:
    destination = "Bulgaria"
    if season == "summer":
        stay = "Camp"
        cost = 30/100 * budget
    elif season == "winter":
        stay = "Hotel"
        cost = 70/100 * budget
elif budget <= 1000:
    destination = "Balkans"
    if season == "summer":
        stay = "Camp"
        cost = 40/100 * budget
    elif season == "winter":
        stay = "Hotel"
        cost = 80/100 * budget
else:
    destination = "Europe"
    cost = 90/100 * budget
    stay = "Hotel"
print(f"Somewhere in {destination}\n{stay} - {cost:.2f}")


