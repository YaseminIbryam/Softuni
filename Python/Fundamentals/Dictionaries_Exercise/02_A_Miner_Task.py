resources_and_quantities = {}
while True:
    command = input()
    if command == "stop":
        for resource, quantity in resources_and_quantities.items():
            print(f"{resource} -> {quantity}")
        break
    resource = command
    quantity = int(input())
    if resource in resources_and_quantities:
        resources_and_quantities[resource] += quantity
    else:
        resources_and_quantities[resource] = quantity
