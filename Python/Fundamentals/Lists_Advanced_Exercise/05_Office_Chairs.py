rooms = int(input())
free_chairs = 0
are_chairs_needed = False
for room in range(1, rooms + 1):
    information = input().split()
    chairs = len(information[0])
    visitors = int(information[1])
    if visitors > chairs:
        are_chairs_needed = True
        needed_chairs = visitors - chairs
        print(f"{needed_chairs} more chairs needed in room {room}")
    elif chairs > visitors:
        free_chairs += chairs - visitors
if not are_chairs_needed:
    print(f"Game On, {free_chairs} free chairs left")