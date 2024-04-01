def add(name: str, quantity: int, area: str):
    if name not in zoo.keys():
        zoo[name] = quantity
        areas[name] = area
    else:
        zoo[name] += quantity


def feed(name: str, quantity: int):
    if name in zoo.keys():
        zoo[name] -= quantity
        if zoo[name] <= 0:
            del zoo[name]
            del areas[name]
            print(f"{name} was successfully fed")


areas = {}
zoo = {}
while True:
    command_list = input().split(': ')
    command = command_list[0]
    if command == 'EndDay':
        break
    info_list = command_list[1].split('-')
    if command == 'Add':
        add(info_list[0], int(info_list[1]), info_list[2])
    elif command == 'Feed':
        feed(info_list[0], int(info_list[1]))
print("Animals:")
for name, quantity in zoo.items():
    print(f" {name} -> {quantity}g")
counts_for_area = {}
for area in areas.values():
    if area in counts_for_area.keys():
        counts_for_area[area] += 1
    else:
        counts_for_area[area] = 1
print("Areas with hungry animals:")
for area, count in counts_for_area.items():
    print(f"{area}: {count}")
