number_locations = int(input())
for location in range(number_locations):
    total_mined_gold_for_location = 0
    expected_average_mining_gold_for_day = float(input())
    number_days_mining_in_location = int(input())
    for day in range(number_days_mining_in_location):
        mined_gold_for_the_day = float(input())
        total_mined_gold_for_location += mined_gold_for_the_day
    average_mined_gold_for_day = total_mined_gold_for_location / number_days_mining_in_location
    if average_mined_gold_for_day >= expected_average_mining_gold_for_day:
        print(f"Good job! Average gold per day: {average_mined_gold_for_day:.2f}.")
    else:
        needed_gold = expected_average_mining_gold_for_day - average_mined_gold_for_day
        print(f"You need {needed_gold:.2f} gold.")
