countries_and_capitals = dict(zip(input().split(', '), input().split(', ')))
for country, capital in countries_and_capitals.items():
    print(f"{country} -> {capital}")
