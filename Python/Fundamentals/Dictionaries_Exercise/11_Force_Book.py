def search_for_user(values, user):
    for value in values:
        if user in value:
            return True
    return False


force_book = {}
while True:
    command = input()
    if command == "Lumpawaroo":
        break
    if '|' in command:
        force_side, force_user = command.split(' | ')
        is_force_user_in_force_book = search_for_user(force_book.values(), force_user)

        if is_force_user_in_force_book:
            continue

        force_book[force_side] = force_book.get(force_side, []) + [force_user]
    elif '->' in command:
        force_user, force_side = command.split(' -> ')
        is_force_user_in_force_book = search_for_user(force_book.values(), force_user)
        if is_force_user_in_force_book:
            for key, value in force_book.items():
                if force_user in value:
                    force_book[key].remove(force_user)

        force_book[force_side] = force_book.get(force_side, []) + [force_user]
        print(f"{force_user} joins the {force_side} side!")
for side, users in force_book.items():
    if len(users) == 0:
        continue
    print(f"Side: {side}, Members: {len(users)}")
    for user in users:
        print(f"! {user}")