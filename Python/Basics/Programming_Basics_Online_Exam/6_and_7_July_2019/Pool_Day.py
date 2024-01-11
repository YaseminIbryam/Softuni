import math

number_people = int(input())
tax = float(input())
price_per_seat = float(input())
price_per_umbrella = float(input())
number_umbrella = math.ceil(number_people / 2)
number_seats = math.ceil(75/100 * number_people)
price_seats = number_seats * price_per_seat
price_umbrellas = number_umbrella * price_per_umbrella
total_tax = tax * number_people
cost = total_tax + price_umbrellas + price_seats
print(f"{cost:.2f} lv.")
