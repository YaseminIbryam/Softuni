price_rating = list(map(int, input().split(', ')))
entry_point = int(input())
type_of_items = input()
if type_of_items == "cheap":
    left_sum = sum([price_rating[index] for index in range(0, entry_point) if price_rating[index] < price_rating[entry_point]])
    right_sum = sum([price_rating[index] for index in range(entry_point + 1, len(price_rating)) if price_rating[index] < price_rating[entry_point]])
else:
    left_sum = sum([price_rating[index] for index in range(0, entry_point) if price_rating[index] >= price_rating[entry_point]])
    right_sum = sum([price_rating[index] for index in range(entry_point + 1, len(price_rating)) if price_rating[index] >= price_rating[entry_point]])
if left_sum >= right_sum:
    print(f"Left - {left_sum}")
else:
    print(f"Right - {right_sum}")
