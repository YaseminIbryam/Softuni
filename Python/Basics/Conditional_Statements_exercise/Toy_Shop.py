puzzle = 2.60
talking_toy = 3
teddy_bear = 4.10
minion = 8.20
truck = 2
price_excursion = float(input())
number_of_puzzles = int(input())
number_of_talking_toys = int(input())
number_of_teddy_bears = int(input())
number_of_minions = int(input())
number_of_trucks = int(input())
number_all_toys = number_of_talking_toys + number_of_trucks + \
                  number_of_minions + number_of_puzzles + number_of_teddy_bears
price_of_puzzles = number_of_puzzles * puzzle
price_of_talking_toys = number_of_talking_toys * talking_toy
price_of_teddy_bears = teddy_bear * number_of_teddy_bears
price_of_minions = minion * number_of_minions
price_of_trucks = number_of_trucks * truck
price_all_toys = price_of_puzzles + price_of_minions + price_of_trucks\
                 + price_of_teddy_bears + price_of_talking_toys
if number_all_toys >= 50:
    price_all_toys = price_all_toys * (1-0.25)
rent = 10/100 * price_all_toys
money = price_all_toys - rent
if money >= price_excursion:
    print(f"Yes! {(money-price_excursion):.2f} lv left.")
else:
    print(f"Not enough money! {(price_excursion-money):.2f} lv needed.")
