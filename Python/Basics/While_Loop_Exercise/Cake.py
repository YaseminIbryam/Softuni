width = int(input())
length = int(input())
cake_size = width * length
cake_finished = False
pieces = 0
command = input()
while command != "STOP" and not cake_finished:
    pieces += int(command)
    if pieces >= cake_size:
        cake_finished = True
        break
    command = input()

if cake_finished:
    needed_pieces = pieces - cake_size
    print(f"No more cake left! You need {needed_pieces} pieces more.")
else:
    pieces_left = cake_size - pieces
    print(f"{pieces_left} pieces are left.")
