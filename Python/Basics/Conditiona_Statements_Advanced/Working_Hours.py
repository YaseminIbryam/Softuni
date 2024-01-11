time = int(input())
day = input()
if day == 'Sunday' or not 10 <= time <= 18:
    print("closed")
else:
    print("open")
