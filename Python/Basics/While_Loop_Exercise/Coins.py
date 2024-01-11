change = round(float(input()), 2)
coins_count = 0
while change > 0:
    if change >= 2:
        change -= 2
    elif change >= 1:
        change -= 1
    elif change >= 0.5:
        change -= 0.5
    elif change >= 0.2:
        change -= 0.2
    elif change >= 0.1:
        change -= 0.1
    elif change >= 0.05:
        change -= 0.05
    elif change >= 0.02:
        change -= 0.02
    elif change >= 0.01:
        change -= 0.01
    coins_count += 1
    change = round(change, 2)
print(coins_count)

# change = float(input())
# cents = int(change * 100)
# coins_count = 0
#
# while cents > 0:
#     if cents >= 200:
#         cents -= 200
#     elif cents >= 100:
#         cents -= 100
#     elif cents >= 50:
#         cents -= 50
#     elif cents >= 20:
#         cents -= 20
#     elif cents >= 10:
#         cents -= 10
#     elif cents >= 5:
#         cents -= 5
#     elif cents >= 2:
#         cents -= 2
#     else:
#         cents -= 1
#     coins_count += 1
#
# print(coins_count)
