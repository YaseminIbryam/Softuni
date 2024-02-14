current_version = list(map(int, input().split(".")))
if current_version[-1] < 9:
    current_version[-1] += 1
else:
    current_version[-1] = 0
    if current_version[-2] < 9:
        current_version[-2] += 1
    else:
        current_version[-2] = 0
        current_version[0] += 1
print(".".join(list(map(str,current_version))))