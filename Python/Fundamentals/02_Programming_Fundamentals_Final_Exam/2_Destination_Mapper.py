import re

places = input()
pattern = r"(\=|\/)(([A-Z][a-zA-Z]{2,})\1)"
# valid_places = re.findall(pattern, places)
# travel_points = sum([len(valid_place) for valid_place in valid_places])
places = re.finditer(pattern, places)
valid_places = [place.group(3) for place in places]

travel_points = sum([len(place) for place in valid_places])
print(f"Destinations: {', '.join(valid_places)}")
print(f"Travel Points: {travel_points}")