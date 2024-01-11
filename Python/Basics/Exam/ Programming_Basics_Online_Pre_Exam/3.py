weight = float(input())
type_service = input()
distance_km = int(input())
price_per_km = 0
total_markup = 0
if type_service == "standard":
    if weight < 1:
        price_per_km = 0.03
    elif weight < 10:
        price_per_km = 0.05
    elif weight < 40:
        price_per_km = 0.10
    elif weight < 90:
        price_per_km = 0.15
    elif weight < 150:
        price_per_km = 0.20
elif type_service == "express":
    markup_for_kg = 0
    if weight < 1:
        price_per_km = 0.03
        markup_for_kg = 0.8 * price_per_km
    elif weight < 10:
        price_per_km = 0.05
        markup_for_kg = 0.4 * price_per_km
    elif weight < 40:
        price_per_km = 0.10
        markup_for_kg = 0.05 * price_per_km
    elif weight < 90:
        price_per_km = 0.15
        markup_for_kg = 0.02 * price_per_km
    elif weight < 150:
        price_per_km = 0.20
        markup_for_kg = 0.01 * price_per_km
    markup_for_km = weight * markup_for_kg
    total_markup = distance_km * markup_for_km
price = price_per_km * distance_km
if type_service == "express":
    price += total_markup
print(f"The delivery of your shipment with weight of {weight:.3f} kg. would cost {price:.2f} lv.")