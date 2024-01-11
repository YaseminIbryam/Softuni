month = input()
nights = int(input())
discount = 0
apartment = 0
studio = 0
if month == "May" or month == "October":
    studio = 50
    apartment = 65
    if nights > 14:
        studio *= (1-30/100)
    elif nights > 7:
        studio *= (1-5/100)
elif month == "June" or month == "September":
    studio = 75.20
    apartment = 68.70
    if nights > 14:
        studio *= (1-20/100)
elif month == "July" or month == "August":
    studio = 76
    apartment = 77
if nights > 14:
    apartment *= (1-10/100)
apartment_total = nights * apartment
studio_total = nights * studio
print(f"Apartment: {apartment_total:.2f} lv.\nStudio: {studio_total:.2f} lv.")
