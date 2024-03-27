def drive(car: str, distance: int, needed_fuel: int):
    if needed_fuel > cars[car]['fuel']:
        print("Not enough fuel to make that ride")
    else:
        cars[car]['mileage'] += distance
        cars[car]['fuel'] -= needed_fuel
        print(f"{car} driven for {distance} kilometers. {needed_fuel} liters of fuel consumed.")
        if cars[car]['mileage'] >= 100_000:
            del cars[car]
            print(f"Time to sell the {car}!")


def refuel(car: str, fuel_refill: int):
    if fuel_refill + cars[car]['fuel'] >= 75:
        fuel_refill = 75 - cars[car]['fuel']
    cars[car]['fuel'] += fuel_refill
    print(f"{car} refueled with {fuel_refill} liters")


def revert(car: str, kilometers: int):
    cars[car]['mileage'] -= kilometers
    if cars[car]['mileage'] < 10_000:
        cars[car]['mileage'] = 10_000
    else:
        print(f"{car} mileage decreased by {kilometers} kilometers")


number_of_cars = int(input())
cars = {}
for new_car in range(number_of_cars):
    car, mileage, fuel = input().split('|')
    cars[car] = {'mileage': int(mileage), 'fuel': int(fuel)}
while True:
    command_list = input().split(' : ')
    if command_list[0] == 'Stop':
        break
    command, car = command_list[0], command_list[1]
    if command == 'Drive':
        drive(car, int(command_list[2]), int(command_list[3]))
    elif command == 'Refuel':
        refuel(car, int(command_list[2]))
    elif command == 'Revert':
        revert(car, int(command_list[2]))
for car in cars:
    print(f"{car} -> Mileage: {cars[car]['mileage']} kms, Fuel in the tank: {cars[car]['fuel']} lt.")