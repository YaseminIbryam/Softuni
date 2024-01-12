centuries = int(input())
years = centuries * 100
days = years * 365.2422
hours = days * 24
minutes = hours * 60
print(f"{centuries} centuries = {round(years)} years = {round(days)} \
days = {round(hours)} hours = {round(minutes)} minutes")
