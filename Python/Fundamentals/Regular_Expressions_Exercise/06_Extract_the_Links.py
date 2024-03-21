import re

pattern = r'((w{3}\.[a-zA-Z0-9\-]+)(\.[a-z]+)+)'
while True:
    text = input()
    if text:
        link = re.search(pattern, text)
        if link:
            print(link.group(1))
    else:
        break
