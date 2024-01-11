number_sold_games = int(input())
Hearthstone = 0
Fornite = 0
Overwatch = 0
Others = 0
for game in range(number_sold_games):
    name_game = input()
    if name_game == "Hearthstone":
        Hearthstone += 1
    elif name_game == "Fornite":
        Fornite += 1
    elif name_game == "Overwatch":
        Overwatch += 1
    else:
        Others += 1

print(f"Hearthstone - {Hearthstone/number_sold_games * 100:.2f}%")
print(f"Fornite - {Fornite/number_sold_games * 100:.2f}%")
print(f"Overwatch - {Overwatch/number_sold_games * 100:.2f}%")
print(f"Others - {Others/number_sold_games * 100:.2f}%")
