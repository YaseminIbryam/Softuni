team_A = [f"A-{player}"for player in range(1, 11 + 1)]
team_B = [f"B-{player}"for player in range(1, 11 + 1)]
cards = input().split()
is_terminated = False
for card in cards:
    if card in team_A:
        team_A.remove(card)
    elif card in team_B:
        team_B.remove(card)
    if len(team_A) < 7 or len(team_B) < 7:
        is_terminated = True
        break
print(f"Team A - {len(team_A)}; Team B - {len(team_B)}")
if is_terminated:
    print("Game was terminated")


