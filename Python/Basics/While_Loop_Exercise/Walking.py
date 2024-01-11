goal = 10000
command = input()
steps = 0
is_goal_reached = False
while command != "Going home":
    steps += int(command)
    if steps >= goal:
        is_goal_reached = True
        break
    command = input()
if command == "Going home":
    command = int(input())
    steps += command
    if steps >= goal:
        is_goal_reached = True
if is_goal_reached:
    print("Goal reached! Good job!")
    print(f"{steps - goal} steps over the goal!")
else:
    print(f"{goal - steps} more steps to reach goal.")
