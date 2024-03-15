message = input()
new_message = ""
for char in message:
    new_message += chr(ord(char) + 3)
print(new_message)