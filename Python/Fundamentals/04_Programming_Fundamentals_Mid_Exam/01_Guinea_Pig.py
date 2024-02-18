quantity_food = float(input())
quantity_hay = float(input())
quantity_cover = float(input())
pigs_weight = float(input())
for day in range(1, 31):
    quantity_food -= 0.3
    if day % 2 == 0:
        quantity_hay -= quantity_food * 0.05
    # if weights is after feeding the pig
    if day % 3 == 0:
        quantity_cover -= 1/3 * pigs_weight
    if not (quantity_hay > 0 and quantity_cover > 0 and quantity_food > 0):
        print("Merry must go to the pet store!")
        break
else:
    print(f"Everything is fine! Puppy is happy! Food: {quantity_food:.2f}, Hay: {quantity_hay:.2f}, Cover: {quantity_cover:.2f}.")