import re


pattern = r'\!([A-Z][a-z]{2,})\!\:\[([a-zA-Z]{8,})\]' # if did not work use \b in start and the end
n = int(input())
for i in range(n):
    message = input()
    message = re.search(pattern, message)
    if message:
        command, string = message.groups()
        print(f"{command}: {' '.join([str(ord(char)) for char in string])}")
    else:
        print("The message is invalid")

# if line 11 didn't work try this instead
"""
ascii_numbers = [str(ord(char)) for char in string]
numbers_str = ' '.join(ascii_numbers)
print(f"{command}: {numbers_str}")
"""


