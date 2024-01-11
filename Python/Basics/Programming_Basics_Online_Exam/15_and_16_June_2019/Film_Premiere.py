projection = input()
packet = input()
tickets = int(input())
price_per_packet = 0
if projection == "John Wick":
    if packet == "Drink":
        price_per_packet = 12
    elif packet == "Popcorn":
        price_per_packet = 15
    elif packet == "Menu":
        price_per_packet = 19
elif projection == "Star Wars":
    if packet == "Drink":
        price_per_packet = 18
    elif packet == "Popcorn":
        price_per_packet = 25
    elif packet == "Menu":
        price_per_packet = 30
    if tickets >= 4:
        price_per_packet *= (1-30/100)
elif projection == "Jumanji":
    if packet == "Drink":
        price_per_packet = 9
    elif packet == "Popcorn":
        price_per_packet = 11
    elif packet == "Menu":
        price_per_packet = 14
    if tickets == 2:
        price_per_packet *= (1-15/100)
bill = price_per_packet * tickets
print(f"Your bill is {bill:.2f} leva.")


