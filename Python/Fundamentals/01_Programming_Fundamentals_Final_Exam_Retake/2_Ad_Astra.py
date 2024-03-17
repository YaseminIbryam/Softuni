import re

pattern = r'(\#|\|)([a-zA-Z\s]+)\1(\d{2}\/\d{2}\/\d{2})\1(\d{1,5})\1'
string = input()
info = re.findall(pattern, string)
total_calories = 0
for item_info in info:
    total_calories += int(item_info[-1])
print(f"You have food to last you for: {total_calories // 2000} days!")
for item_info in info:
    print(f"Item: {item_info[1]}, Best before: {item_info[2]}, Nutrition: {item_info[3]}")
