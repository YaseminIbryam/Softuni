number_days = int(input())
total_degrees = 0
total_brandy = 0
for day in range(number_days):
    liters_brandy = float(input())
    degrees = float(input())
    total_degrees += liters_brandy * degrees
    total_brandy += liters_brandy
average_degrees = total_degrees/total_brandy
print(f"Liter: {total_brandy:.2f}")
print(f"Degrees: {average_degrees:.2f}")
if average_degrees < 38:
    print("Not good, you should baking!")
elif 38 <= average_degrees <= 42:
    print("Super!")
elif average_degrees > 42:
    print("Dilution with distilled water!")
