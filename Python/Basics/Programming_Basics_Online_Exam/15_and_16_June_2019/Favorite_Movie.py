from sys import maxsize
command = input()
number_movies = 0
max_points = -maxsize
best_movie = ""
while command != "STOP":
    name_movie = command
    points = 0
    number_movies += 1
    for index, symbol in enumerate(name_movie):
        points += ord(symbol)
        if symbol.isspace():
            continue
        elif symbol.isupper():
            points -= len(name_movie)
        elif symbol.islower():
            points -= 2*len(name_movie)
    if max_points < points:
        max_points = points
        best_movie = name_movie
    if number_movies == 7:
        print("The limit is reached.")
        break
    command = input()
print(f"The best movie for you is {best_movie} with {max_points} ASCII sum.")
