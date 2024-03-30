def plunder(town: str, people: int, gold: int):
    cities[town]['population'] -= people
    cities[town]['gold'] -= gold
    print(f"{town} plundered! {gold} gold stolen, {people} citizens killed.")
    if cities[town]['population'] == 0 or cities[town]['gold'] == 0:
        del cities[town]
        print(f"{town} has been wiped off the map!")


def prosper(town: str, gold: int):
    if gold > 0:
        cities[town]['gold'] += gold
        print(f"{gold} gold added to the city treasury. {town} now has {cities[town]['gold']} gold.")
    elif gold < 0:
        print('Gold added cannot be a negative number!')


cities = {}
while True:
    command = input().split('||')
    if command[0] == 'Sail':
        break
    city, population, gold = command
    if city in cities:
        cities[city]['population'] += int(population)
        cities[city]['gold'] += int(gold)
    else:
        cities[city] = {'population': int(population), 'gold': int(gold)}

while True:
    command = input().split('=>')
    if command[0] == 'End':
        break
    if command[0] == 'Plunder':
        plunder(command[1], int(command[2]), int(command[3]))
    elif command[0] == 'Prosper':
        prosper(command[1], int(command[2]))
if cities:
    print(f"Ahoy, Captain! There are {len(cities)} wealthy settlements to go to:")
    for city, info in cities.items():
        print(f"{city} -> Population: {info['population']} citizens, Gold: {info['gold']} kg")
else:
    print("Ahoy, Captain! All targets have been plundered and destroyed!")