import re

n = int(input())
pattern = r'(.+)\>(\d{3})\|([a-z]{3})\|([A-Z]{3})\|([^\<\>]{3})\<\1'
for i in range(n):
    password = input()
    valid_password = re.search(pattern, password)
    if valid_password:
        start, *encrypted_password_list = valid_password.groups()
        encrypted_password = ''.join(encrypted_password_list)
        print(f"Password: {encrypted_password}")
    else:
        print("Try another password!")
