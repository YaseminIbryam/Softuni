from collections import deque

cups = deque(map(int, input().split()))
bottles = list(map(int, input().split()))
wasted_water = 0
while cups:
    bottle = bottles.pop()
    cup = cups.popleft()
    if bottle >= cup:
        bottle -= cup
        wasted_water += bottle
        bottle = 0
    else:
        cup -= bottle
        while cup > 0:
            bottle = bottles.pop()
            if bottle >= cup:
                bottle -= cup
                wasted_water += bottle
                break
            else:
                cup -= bottle
            if not bottles:
                break
    if not bottles:
        print('Cups:', end=' ')
        while cups:
            print(cups.popleft(), end=' ')
        break
else:
    print('Bottles:', end=' ')
    while bottles:
        print(bottles.pop(), end=' ')
print(f"\nWasted litters of water: {wasted_water}")