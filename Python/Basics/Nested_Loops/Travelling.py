command = input()
while command != "End":
    saved_money = 0
    min_budget = float(input())
    destination = command
    while saved_money < min_budget:
        money = float(input())
        saved_money += money
    print(f"Going to {destination}!")
    command = input()



