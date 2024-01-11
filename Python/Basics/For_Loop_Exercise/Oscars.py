name_of_actor = input()
points = float(input())
number_of_appraisers = int(input())
for appraiser in range(number_of_appraisers):
    name_of_appraiser = input()
    points_from_appraiser = float(input())
    points += len(name_of_appraiser) * points_from_appraiser / 2
    if points > 1250.5:
        print(f"Congratulations, {name_of_actor} got a nominee for leading role with {points:.1f}!")
        break
if points < 1250.5:
    needed_points = 1250.5 - points
    print(f"Sorry, {name_of_actor} you need {needed_points:.1f} more!")
