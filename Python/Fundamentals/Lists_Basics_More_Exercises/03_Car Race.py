numbers = list(map(int, input().split()))
finish_line = len(numbers) // 2
left_side = numbers[:finish_line]
right_side = numbers[:finish_line:-1]
time_left_side = 0
for number in left_side:
    if number == 0:
        time_left_side = time_left_side * 0.8
    time_left_side += number
time_right_side = 0
for number in right_side:
    if number == 0:
        time_right_side = time_right_side * 0.8
    time_right_side += number
if time_left_side < time_right_side:
    winner = "left"
    winner_time = time_left_side
else:
    winner = "right"
    winner_time = time_right_side
print(f"The winner is {winner} with total time: {winner_time:.1f}")


