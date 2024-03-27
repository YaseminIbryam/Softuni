def rate(plant: str, rating: float):
    if 'rating' in plants[plant]:
        plants[plant]['rating'] += [rating]
    else:
        plants[plant]['rating'] = [rating]


def update(plant: str, new_rarity: int):
    plants[plant]['rarity'] = int(new_rarity)


def reset(plant: str):
    if 'rating' in plants[plant]:
        plants[plant]['rating'].clear()


lines = int(input())
plants = {}
for line in range(lines):
    plant, rarity = input().split('<->')
    if plant not in plants.keys():
        plants[plant] = {}
    plants[plant]["rarity"] = int(rarity)
while True:
    command_list = input()
    if command_list == 'Exhibition':
        break
    command_list = command_list.split(': ')
    command = command_list[0]
    info_list = command_list[1].split(' - ')
    plant = info_list[0]
    if plant not in plants.keys():
        print('error')
    elif command == 'Rate':
        rate(plant, float(info_list[1]))
    elif command == 'Update':
        update(plant, int(info_list[1]))
    elif command == 'Reset':
        reset(plant)
print("Plants for the exhibition:")
for plant, value in plants.items():
    if 'rating' in value.keys() and len(value['rating']) > 0:
        average_rating = sum(value['rating']) / len(value['rating'])
    else:
        average_rating = 0
    print(f"- {plant}; Rarity: {value['rarity']}; Rating: {average_rating:.2f}")
