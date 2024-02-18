def travel(light_years):
    is_mission_failed = False
    if light_years > amount_fuel:
        is_mission_failed = True
    return is_mission_failed, light_years


def enemy(enemy_armour, ammunition, fuel):
    is_mission_failed = False
    if ammunition >= enemy_armour:
        ammunition -= enemy_armour
        message =  f"An enemy with {enemy_armour} armour is defeated."
    elif fuel >= enemy_armour * 2:
        fuel -= enemy_armour * 2
        message = f"An enemy with {enemy_armour} armour is outmaneuvered."
    else:
        is_mission_failed = True
        fuel -= fuel
        message = "Mission failed."
    return is_mission_failed, message, ammunition, fuel


def repair(added_fuel_and_ammunition, ammunition, fuel):
    added_fuel = added_fuel_and_ammunition
    added_ammunition = added_fuel_and_ammunition * 2
    fuel += added_fuel
    ammunition += added_ammunition
    message = f"Ammunitions added: {added_ammunition}.\nFuel added: {added_fuel}."
    return message, ammunition, fuel

def titan():
    return "You have reached Titan, all passengers are safe."





travel_route = input().split("||")
amount_fuel = int(input())
amount_ammunition = int(input())
for command_list in travel_route:
    command_list = command_list.split()
    command = command_list[0]
    if command == "Travel":
        integer = int(command_list[1])
        is_mission_failed, light_years = travel(integer)
        if is_mission_failed:
            print("Mission failed.")
            break
        else:
            amount_fuel -= light_years
            print(f"The spaceship travelled {light_years} light-years.")
    elif command == "Enemy":
        integer = int(command_list[1])
        is_mission_failed, message, amount_ammunition, amount_fuel = enemy(integer, amount_ammunition, amount_fuel)
        print(message)
        if is_mission_failed:
            break
    elif command == "Repair":
        integer = int(command_list[1])
        message, amount_ammunition, amount_fuel = repair(integer, amount_ammunition, amount_fuel)
        print(message)
    elif command == "Titan":
        print(titan())
        break





