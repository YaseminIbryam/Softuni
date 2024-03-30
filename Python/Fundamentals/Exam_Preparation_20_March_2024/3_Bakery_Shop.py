def receive(quantity: int, food: str):
    if quantity > 0:
        if food in bakery:
            bakery[food] += quantity
        else:
            bakery[food] = quantity


def sell(quantity: int, food: str):
    sold = 0
    if food not in bakery:
        print(f"You do not have any {food}.")
    elif quantity > bakery[food]:
        print(f"There aren't enough {food}. You sold the last {bakery[food]} of them.")
        sold += bakery[food]
        del bakery[food]
    else:
        bakery[food] -= quantity
        print(f"You sold {quantity} {food}.")
        sold += quantity
        if bakery[food] == 0:
            del bakery[food]
    return sold


bakery = {}
sold = 0
while True:
    command = input().split()
    if command[0] == "Complete":
        break
    if command[0] == "Receive":
        receive(int(command[1]), command[2])
    elif command[0] == "Sell":
        sold += sell(int(command[1]), command[2])
for food, quantity in bakery.items():
    print(f"{food}: {quantity}")
print(f"All sold: {sold} goods")