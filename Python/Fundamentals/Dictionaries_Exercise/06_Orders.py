orders = {}
while True:
    command = input()
    if command == "buy":
        for name, total_price in orders.items():
            print(f"{name} -> {(total_price['price'] * total_price['quantity']):.2f}")
        break
    command = command.split()
    name, price, quantity = command[0], float(command[1]), int(command[2])
    if name in orders.keys():
        orders[name]['price'] = price
        orders[name]['quantity'] += quantity
    else:
        orders[name] = {"price": price, "quantity": quantity}

