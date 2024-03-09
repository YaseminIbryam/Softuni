usernames = input().split(', ')
for username in usernames:
    if 3 <= len(username) <= 16:
        for char in username:
            if not (char.isalpha() or char.isdigit() or char == '_' or char == '-'):
                break
        else:
            print(username)