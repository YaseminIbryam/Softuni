price_bullet = int(input())
size_gun_barrel = int(input())
bullets = list(map(int, input().split()))
locks = (list(map(int, input().split())))[::-1]
value_intelligence = int(input())
used_bullets = 0
while True:
    if not bullets:
        print(f"Couldn't get through. Locks left: {len(locks)}")
        break
    bullet = bullets.pop()
    used_bullets += 1
    lock = locks.pop()
    if bullet <= lock:
        print('Bang!')
    else:
        print('Ping!')
        locks.append(lock)
    if used_bullets % size_gun_barrel == 0 and bullets:
        print('Reloading!')
    if not locks:
        bullets_cost = used_bullets * price_bullet
        money_earned = value_intelligence - bullets_cost
        print(f"{len(bullets)} bullets left. Earned ${money_earned}")
        break

