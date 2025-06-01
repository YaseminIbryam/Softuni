N = int(input())
cars = set()
for i in range(N):
    direction, car_number = input().split(', ')
    if direction == 'IN':
        cars.add(car_number)
    elif direction == 'OUT':
        cars.discard(car_number)
if cars:
    for car in cars:
        print(car)
else:
    print("Parking Lot is Empty")
