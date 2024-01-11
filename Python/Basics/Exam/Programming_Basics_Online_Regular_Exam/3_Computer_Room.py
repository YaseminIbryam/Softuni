month = input()
number_hours = int(input())
number_people = int(input())
time_of_the_day = input()
price_per_hour = 0
if month == "march" or month == "april" or month == "may":
    if time_of_the_day == "day":
        price_per_hour = 10.5
    elif time_of_the_day == "night":
        price_per_hour = 8.4
elif month == "june" or month == "july" or month == "august":
    if time_of_the_day == "day":
        price_per_hour = 12.6
    elif time_of_the_day == "night":
        price_per_hour = 10.2
if number_people >= 4:
    price_per_hour *= 0.9
if number_hours >= 5:
    price_per_hour *= 0.5
price_per_person = price_per_hour * number_hours
print(f"Price per person for one hour: {price_per_hour:.2f}")
bill = price_per_person * number_people
print(f"Total cost of the visit: {bill:.2f}")



