time1 = int(input())
time2 = int(input())
time3 = int(input())
time = time1 + time2 + time3
time_m = time//60
time_s = time % 60
if time_s < 10:
    time_s = "0" + str(time_s)
print(f"{time_m}:{time_s}")
