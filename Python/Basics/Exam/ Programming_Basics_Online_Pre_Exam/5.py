meters = 5364
days = 1
while meters < 8848:
    command = input()
    if command == "END":
        break
    meters_climbed = int(input())
    if command == "Yes":
        days += 1
        if days > 5:
            break
    meters += meters_climbed
    if meters >= 8848:
        break
if meters >= 8848:
    print(f"Goal reached for {days} days!")
else:
    print("Failed!")
    print(f"{meters}")
