# import re
#
# regex = r"\d+"
# numbers = []
# while True:
#     text = input()
#     if text != '':  # if not line:
#         numbers += re.findall(regex, text)
#     else:
#         break
# print(" ".join(numbers))

import re

line = input()
while line:
    pattern = "\d+"
    matches = re.findall(pattern, line)
    if matches:
        print(" ".join(matches), end=" ")
    line = input()

