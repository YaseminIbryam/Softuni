experience_needed = float(input())
battles = int(input())
gained_experience = 0
for battle in range(1, battles + 1):
    experience = float(input())
    # if percents are from one to another
    if battle % 3 == 0:
        experience += experience * 0.15
    if battle % 5 == 0:
        experience -= experience * 0.1
    if battle % 15 == 0:
        experience += experience * 0.05
    gained_experience += experience
    if gained_experience >= experience_needed:
        # it is asking for the battle we just finished not all count
        print(f"Player successfully collected his needed experience for {battle} battles.")
        break
else:
    more_needed_experience = experience_needed - gained_experience
    print(f"Player was not able to collect the needed experience, {more_needed_experience:.2f} more needed.")
