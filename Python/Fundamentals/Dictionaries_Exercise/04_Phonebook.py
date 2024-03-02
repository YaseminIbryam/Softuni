phonebook = {}
while True:
    entry = input()
    if entry.isnumeric():
        number = int(entry)
        for person in range(number):
            person_name = input()
            if person_name in phonebook.keys():
                print(f"{person_name} -> {phonebook[person_name]}")
            else:
                print(f"Contact {person_name} does not exist.")
        break
    name, phone_number = entry.split('-')
    phonebook[name] = phone_number
