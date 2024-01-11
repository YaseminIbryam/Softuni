from math import floor

number_of_tournaments = int(input())
start_points = int(input())
points_of_tournaments = 0
number_of_tournaments_with_win = 0
for tournament in range(number_of_tournaments):
    stage = input()
    if stage == "W":
        number_of_tournaments_with_win += 1
        points_of_tournaments += 2000
    elif stage == "F":
        points_of_tournaments += 1200
    elif stage == "SF":
        points_of_tournaments += 720
total_points = start_points + points_of_tournaments
average_points_per_tournament = points_of_tournaments / number_of_tournaments
percent_tournaments_with_win = number_of_tournaments_with_win / number_of_tournaments * 100
print(f"Final points: {total_points}")
print(f"Average points: {floor(average_points_per_tournament)}")
print(f"{percent_tournaments_with_win:.2f}%")
