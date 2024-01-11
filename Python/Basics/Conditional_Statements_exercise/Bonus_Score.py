start_points = int(input())
if start_points <= 100:
    bonus_points = 5
elif 1000 >= start_points > 100:
    bonus_points = start_points * 20/100
else:
    bonus_points = start_points * 10/100
if start_points % 2 == 0:
    bonus_points += 1
elif start_points % 10 == 5:
    bonus_points += 2
print(bonus_points)
print(bonus_points + start_points)
