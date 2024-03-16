import re

text = input()
regex = fr"(?i)\b{input()}\b"
matches = re.findall(regex, text)
# matches = re.findall(regex, text, re.I)
print(len(matches))
