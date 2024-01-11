number_of_holidays = int(input())
norm = 30000
time_for_play = number_of_holidays * 127 + (365 - number_of_holidays) * 63
diff = abs(time_for_play - norm)
hours = diff // 60
minutes = diff % 60
if time_for_play > norm:
    print("Tom will run away")
    print(f"{hours} hours and {minutes} minutes more for play")
elif time_for_play < norm:
    print("Tom sleeps well")
    print(f"{hours} hours and {minutes} minutes less for play")
