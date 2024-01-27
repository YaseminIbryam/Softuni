events = input().split("|")
energy, coins = 100, 100
for event in events:
    name_event, number = event.split("-")
    number = int(number)
    if name_event == "rest":
        initial_energy = energy
        energy += number
        if energy > 100:
            energy = 100
        gained_energy = energy - initial_energy
        print(f"You gained {gained_energy} energy.")
        print(f"Current energy: {energy}.")
    elif name_event == "order":
        if energy >= 30:
            energy -= 30
            coins += number
            print(f"You earned {number} coins.")
        else:
            print("You had to rest!")
            energy += 50
    else:
        ingredient = name_event
        if coins >= number:
            coins -= number
            print(f"You bought {ingredient}.")
        else:
            print(f"Closed! Cannot afford {ingredient}.")
            break
else:
    print("Day completed!")
    print(f"Coins: {coins}")
    print(f"Energy: {energy}")




