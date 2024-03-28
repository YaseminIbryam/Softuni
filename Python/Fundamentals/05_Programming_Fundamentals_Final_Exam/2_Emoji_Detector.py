import re

text = input()
emoji_pattern = r'(\:|\*)\1([A-Z][a-z]{2,})\1{2}'
digits = list(map(int, [digit for digit in text if digit.isdigit()]))
threshold = 1
for digit in digits:
    threshold *= digit
emojis = re.finditer(emoji_pattern, text)
valid_emojis = [emoji.group() for emoji in emojis]
print(f"Cool threshold: {threshold}")
print(f"{len(valid_emojis)} emojis found in the text. The cool ones are:")
for emoji in valid_emojis:
    coolness = 0
    for char in emoji:
        if char.isalpha():
            coolness += ord(char)
    if coolness >= threshold:
        print(emoji)
