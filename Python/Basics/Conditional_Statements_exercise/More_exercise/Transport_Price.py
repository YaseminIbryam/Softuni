kilometers = int(input())
time_of_the_day = input()  # day or night
price_transport = 0
if kilometers < 20:
    if time_of_the_day == "day":
        price_transport = 0.70 + kilometers * 0.79
    elif time_of_the_day == "night":
        price_transport = 0.70 + kilometers * 0.90
elif 20 <= kilometers < 100:
    price_transport = kilometers * 0.09
else:
    price_transport = kilometers * 0.06
print(f"{price_transport:.2f}")
