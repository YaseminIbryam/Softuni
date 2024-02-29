def add_to_dict(key, value, dictionary):
    if key in dictionary.keys():
        dictionary[key] += value
        return dictionary
    dictionary[key] = value
    return dictionary


statistics_dict = {}
while True:
    command = input()
    if command == "statistics":
        break
    command = command.split()
    add_to_dict(command[0], int(command[1]), statistics_dict)
print("Products in stock:")
for product, quantity in statistics_dict.items():
    print(f"- {product} {quantity}")
print(f"Total Products: {len(statistics_dict.keys())}\nTotal Quantity: {sum(statistics_dict.values())}")
