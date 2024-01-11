budget_actors = float(input())
command = input()
left_budget = budget_actors
while command != "ACTION" and left_budget > 0:
    name_actor = command
    if len(name_actor) <= 15:
        salary = float(input())
    else:
        salary = left_budget * 0.2
    left_budget -= salary
    if left_budget > 0:
        command = input()
if left_budget > 0:

    print(f"We are left with {left_budget:.2f} leva.")
else:
    needed_budget = abs(left_budget)
    print(f"We need {needed_budget:.2f} leva for our actors.")
