length = int(input())
width = int(input())
height = int(input())
percent_not_empty = float(input()) / 100
fish_tank_volume = length * width * height
volume_in_litres = fish_tank_volume / 1000
needed_litres = volume_in_litres * (1 - percent_not_empty)
print(needed_litres)
