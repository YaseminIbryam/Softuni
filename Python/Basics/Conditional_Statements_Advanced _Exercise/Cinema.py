type_of_projection = input()
rows = int(input())
columns = int(input())
seats = rows * columns
income = 0
if type_of_projection == "Premiere":
    income = seats * 12.00
elif type_of_projection == "Normal":
    income = seats * 7.50
elif type_of_projection == "Discount":
    income = seats * 5.00
print(f"{income:.2f} leva")

