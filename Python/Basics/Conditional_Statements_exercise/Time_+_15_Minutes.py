hour = int(input())
minutes = int(input())
if minutes < 45:
    minutes = minutes + 15
elif hour < 23:
    hour += 1
    minutes = (minutes + 15) % 60
    if minutes < 10:
        minutes = "0" + str(minutes)
else:
    hour = 0
    minutes = (minutes + 15) % 60
    if minutes < 10:
        minutes = "0" + str(minutes)
print(f"{hour}:{minutes}")
