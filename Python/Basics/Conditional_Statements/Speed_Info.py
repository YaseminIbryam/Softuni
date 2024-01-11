v = float(input())
if v <= 10:
    print("slow")
elif 10 < v <= 50:
    print("average")
elif 50 < v <= 150:
    print("fast")
elif 150 < v <= 1000:
    print("ultra fast")
elif 1000 < v:
    print("extremely fast")
