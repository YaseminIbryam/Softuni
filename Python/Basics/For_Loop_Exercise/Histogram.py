count_numbers = int(input())
less_than_200 = 0
between_200_399 = 0
between_400_599 = 0
between_600_799 = 0
over_800 = 0
for i in range(count_numbers):
    number = int(input())
    if number < 200:
        less_than_200 += 1
    elif 200 <= number < 400:
        between_200_399 += 1
    elif 400 <= number < 600:
        between_400_599 += 1
    elif 600 <= number < 800:
        between_600_799 += 1
    elif number >= 800:
        over_800 += 1
percent_1 = less_than_200 / count_numbers * 100
percent_2 = between_200_399 / count_numbers * 100
percent_3 = between_400_599 / count_numbers * 100
percent_4 = between_600_799 / count_numbers * 100
percent_5 = over_800 / count_numbers * 100
print(f"{percent_1:.2f}%")
print(f"{percent_2:.2f}%")
print(f"{percent_3:.2f}%")
print(f"{percent_4:.2f}%")
print(f"{percent_5:.2f}%")
