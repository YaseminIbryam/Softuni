number_of_quantity = int(input())
type_of_quantity = input()
delivery_option = input()
type_90X130 = 110
type_100X150 = 140
type_130X180 = 190
type_200X300 = 250
price_of_quantity = 0
if number_of_quantity < 10:
    print("Invalid order")
if type_of_quantity == "90X130":
    if 60 >= number_of_quantity > 30:
        price_of_quantity = type_90X130 - type_90X130 * 5 / 100
    elif number_of_quantity > 60:
        price_of_quantity = type_90X130 - type_90X130 * 8 / 100
    elif number_of_quantity <= 30:
        price_of_quantity = type_90X130
elif type_of_quantity == "100X150":
    if 80 >= number_of_quantity > 40:
        price_of_quantity = type_100X150 - type_100X150 * 6 / 100
    elif number_of_quantity > 80:
        price_of_quantity = type_100X150 - type_100X150 * 10 / 100
    elif number_of_quantity <= 40:
        price_of_quantity = type_100X150
elif type_of_quantity == "130X180":
    if 50 >= number_of_quantity > 20:
        price_of_quantity = type_130X180 - type_130X180 * 7 / 100
    elif number_of_quantity > 50:
        price_of_quantity = type_130X180 - type_130X180 * 12 / 100
    elif number_of_quantity <= 20:
        price_of_quantity = type_130X180
elif type_of_quantity == "200X300":
    if 50 >= number_of_quantity > 25:
        price_of_quantity = type_200X300 - type_200X300 * 9 / 100
    elif number_of_quantity > 50:
        price_of_quantity = type_200X300 - type_200X300 * 14 / 100
    elif number_of_quantity <= 25:
        price_of_quantity = type_200X300

price = price_of_quantity * number_of_quantity
if delivery_option == "With delivery":
    price = price + 60
if number_of_quantity > 99:
    price = price - price * 4 / 100
if number_of_quantity >= 10:
    print(f"{price:.2f} BGN")
