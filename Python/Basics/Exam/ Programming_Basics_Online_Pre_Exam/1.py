number_people = int(input())
number_nights = int(input())
number_carts = int(input())
number_tickets = int(input())
night_price = 20
cart_price = 1.60
ticket_price = 6
price_per_person = night_price * number_nights + cart_price * number_carts + ticket_price * number_tickets
price = price_per_person * number_people
total_cost = price * (1+0.25)
print(f"{total_cost:.2f}")