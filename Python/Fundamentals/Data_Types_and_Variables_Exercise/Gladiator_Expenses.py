lost_fights_count = int(input())
helmet_price = float(input())
sword_price = float(input())
shield_price = float(input())
armor_price = float(input())
expenses = 0
shield_breaking_count = 0
for lost_fight in range(1, lost_fights_count + 1):
    if lost_fight % 2 == 0:
        expenses += helmet_price
    if lost_fight % 3 == 0:
        expenses += sword_price
        if lost_fight % 2 == 0:
            expenses += shield_price
            shield_breaking_count += 1
            if shield_breaking_count == 2:
                shield_breaking_count = 0
                expenses += armor_price
print(f"Gladiator expenses: {expenses:.2f} aureus")

