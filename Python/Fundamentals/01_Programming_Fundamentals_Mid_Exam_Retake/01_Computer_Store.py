command = input()
total_price = 0
while command != "regular" and command != "special":
    price = float(command)
    if price < 0:
        print("Invalid price!")
        command = input()
        continue
    total_price += price
    command = input()
taxes = total_price * 0.2
price_with_taxes = total_price + taxes
if total_price == 0:
    print("Invalid order!")
else:
    if command == "special":
        price_with_taxes -= price_with_taxes * 0.1
    print(f"Congratulations you've just bought a new computer!\nPrice without taxes: {total_price:.2f}$\nTaxes: {taxes:.2f}$")
    print("-----------")
    print(f"Total price: {price_with_taxes:.2f}$")

