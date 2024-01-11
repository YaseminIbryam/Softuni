time_filming = int(input())
number_scenes = int(input())
time_scene = int(input())
preparation = 15/100 * time_filming
time_needed = time_scene * number_scenes + preparation
if time_filming >= time_needed:
    time_left = time_filming - time_needed
    print(f"You managed to finish the movie on time! You have {round(time_left)} minutes left!")
else:
    more_time_needed = time_needed - time_filming
    print(f"Time is up! To complete the movie you need {round(more_time_needed)} minutes.")