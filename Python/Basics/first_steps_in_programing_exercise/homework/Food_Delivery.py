chicken_menu = 10.35
fish_menu = 12.40
vegetarian_menu = 8.15
number_of_chicken = int(input())
number_of_fish = int(input())
number_of_vegetarians = int(input())
price_of_chicken = chicken_menu * number_of_chicken
price_of_fish = fish_menu * number_of_fish
price_of_vegetarian = vegetarian_menu * number_of_vegetarians
total_price_of_menus = price_of_chicken + price_of_vegetarian + price_of_fish
price_of_desert = total_price_of_menus * 0.20
delivery = 2.50
bill = total_price_of_menus + price_of_desert + delivery
print(bill)
