gasoline_price_per_liter = 2.22
diesel_price_per_liter = 2.33
gas_price_per_liter = 0.93
type_fuel = input()
liters_fuel = int(input())
club_card = input()  # yes or no
price = 0
if club_card == "Yes":
    gasoline_price_per_liter -= 0.18
    diesel_price_per_liter -= 0.12
    gas_price_per_liter -= 0.08
if type_fuel == "Gasoline":
    price = gasoline_price_per_liter * liters_fuel
elif type_fuel == "Diesel":
    price = diesel_price_per_liter * liters_fuel
elif type_fuel == "Gas":
    price = gas_price_per_liter * liters_fuel
if 20 < liters_fuel <= 25:
    price -= price * 8/100
elif liters_fuel > 25:
    price -= price * 10/100
print(f"{price:.2f} lv.")
