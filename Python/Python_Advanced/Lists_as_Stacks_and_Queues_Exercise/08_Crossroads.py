from collections import deque

green_light = int(input())
free_window = int(input())
cars = deque()
number_cars = 0
crash = False
while True:
    command = input()
    if command == 'END':
        print("Everyone is safe.")
        print(f"{number_cars} total cars passed the crossroads.")
        break
    elif command == 'green':
        green_light_time = green_light
        free_window_time = free_window
        while green_light_time > 0:
            if not cars:
                break
            car = cars.popleft()
            if len(car) > green_light_time + free_window_time:
                index = green_light_time + free_window_time
                print('A crash happened!')
                print(f"{car} was hit at {car[index]}.")
                crash = True
                break
            green_light_time -= len(car)
            number_cars += 1
        if crash:
            break
    cars.append(command)