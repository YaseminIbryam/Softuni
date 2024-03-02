chars_count = {}
text = input()
for char in text:
    if not char.isspace():
        if char not in chars_count.keys():
            chars_count[char] = text.count(char)
for char, count in chars_count.items():
    print(f"{char} -> {count}")
