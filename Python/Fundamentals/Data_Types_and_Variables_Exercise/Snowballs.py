number_snowballs = int(input())
snowball_weight = 0
snowball_time = 0
snowball_value = 0
snowball_quality = 0
for snowball in range(number_snowballs):
    weight = int(input())
    time = int(input())
    quality = int(input())
    value = (weight / time) ** quality
    if value > snowball_value:
        snowball_value = value
        snowball_quality = quality
        snowball_time = time
        snowball_weight = weight
print(f"{snowball_weight} : {snowball_time} = {int(snowball_value)} ({snowball_quality})")
