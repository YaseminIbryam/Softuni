from collections import deque


def seconds_to_time(total_seconds):
    m, s = divmod(total_seconds, 60)
    h, m = divmod(m, 60)
    if h >= 24:
        h -= 24
    return f'[{h:02}:{m:02}:{s:02}]'

robots_info = input().split(';')
robots = {}
robots_names = deque()
for robot in robots_info:
    name, time = robot.split('-')
    robots_names.append(name)
    robots[name] = int(time)
robots_copy = robots.copy()
starting_time = input().split(':')
start_h, start_m, start_s = map(int, starting_time)
total_seconds_start = start_h * 3600 + start_m * 60 + start_s
products = deque()
while True:
    product = input()
    if product == 'End':
        break
    products.append(product)
seconds = 0
while products:
    seconds += 1
    for key, value in robots_copy.items():
        robots_copy[key] = value + 1
    product = products.popleft()
    for robot in robots_names:
        if robots[robot] <= robots_copy[robot]:
            total_seconds = total_seconds_start + seconds
            time = seconds_to_time(total_seconds)
            print(f'{robot} - {product} {time}')
            robots_copy[robot] = 0
            break
    else:
        products.append(product)


