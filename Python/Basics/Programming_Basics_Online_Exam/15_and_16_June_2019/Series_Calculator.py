from math import floor
name_series = input()
number_seasons = int(input())
number_episodes = int(input())
time_episode = float(input())
total_time_episode = (1 + 20/100) * time_episode
total_time_for_season = total_time_episode * number_episodes + 10
total_time = total_time_for_season * number_seasons
print(f"Total time needed to watch the {name_series} series is {floor(total_time)} minutes.")
