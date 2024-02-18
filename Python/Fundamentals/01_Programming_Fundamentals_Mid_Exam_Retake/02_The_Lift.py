people = int(input())
current_state = list(map(int, input().split()))
for index, wagon in enumerate(current_state):
    while wagon < 4:
        wagon += 1
        people -= 1
        current_state[index] = wagon
        if people == 0:
            break
    if people == 0:
        for lift in current_state:
            if lift != 4:
                print("The lift has empty spots!")
                break
        print(" ".join(list(map(str, current_state))))
        break
else:
    print(f"There isn't enough space! {people} people in a queue!")
    print(" ".join(list(map(str, current_state))))

