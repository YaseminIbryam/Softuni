rose = 5
dahlia = 3.80
tulip = 2.80
narcissus = 3
gladiolus = 2.50
type_of_flowers = input()
number_of_flowers = int(input())
budget = int(input())
price = 0
if type_of_flowers == "Roses":
    price = number_of_flowers * rose
    if number_of_flowers > 80:
        price *= 90/100
elif type_of_flowers == "Dahlias":
    price = number_of_flowers * dahlia
    if number_of_flowers > 90:
        price *= 85/100
elif type_of_flowers == "Tulips":
    price = number_of_flowers * tulip
    if number_of_flowers > 80:
        price *= 85/100
elif type_of_flowers == "Narcissus":
    price = number_of_flowers * narcissus
    if number_of_flowers < 120:
        price *= 115/100
elif type_of_flowers == "Gladiolus":
    price = number_of_flowers * gladiolus
    if number_of_flowers < 80:
        price *= 120/100
if budget >= price:
    left_money = budget - price
    print(f"Hey, you have a great garden with {number_of_flowers} {type_of_flowers} and {left_money:.2f} leva left.")
else:
    needed_money = price - budget
    print(f"Not enough money, you need {needed_money:.2f} leva more.")
