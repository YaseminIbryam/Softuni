days = int(input())
type_stay = input()
evaluation = input()
cost_per_day = 0
discount = 0
nights = days - 1
total_cost = 0
if type_stay == "room for one person":
    cost_per_day = 18.00
elif type_stay == "apartment":
    cost_per_day = 25.00
    if days < 10:
        discount = 0.30
    elif days <= 15:
        discount = 0.35
    elif days > 15:
        discount = 0.50
elif type_stay == "president apartment":
    cost_per_day = 35.00
    if days < 10:
        discount = 0.10
    elif days <= 15:
        discount = 0.15
    elif days > 15:
        discount = 0.20
cost = cost_per_day * (1 - discount) * nights
if evaluation == "positive":
    total_cost = cost * (1 + 0.25)
elif evaluation == "negative":
    total_cost = cost * (1 - 0.10)
print(f"{total_cost:.2f}")
