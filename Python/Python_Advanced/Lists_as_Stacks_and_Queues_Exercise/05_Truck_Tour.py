from collections import deque
petrol_pumps = int(input())

petrol_pumps_queue = deque()
for petrol_pump in range(petrol_pumps):
    amount_petrol, distance = input().split()
    amount_petrol, distance = float(amount_petrol), float(distance)
    petrol_pumps_queue.append((amount_petrol, distance))
start_found = False
start = 0
while not start_found:
    total_petrol = 0
    for amount_petrol, distance in petrol_pumps_queue:
        total_petrol += amount_petrol
        if total_petrol >= distance:
            total_petrol -= distance
        else:
            petrol_pumps_queue.append(petrol_pumps_queue.popleft())
            break
    else:
        start_found = True
        break
    start += 1
print(start)