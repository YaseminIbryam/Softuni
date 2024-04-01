def illusion(index: int, letter: str):
    if 0 > index or index >= len(spell):
        print("The spell was too weak.")
    else:
        return spell[:index] + letter + spell[index+1:]


def divination(first_substring: str, second_substring: str):
    if first_substring in spell:
        return spell.replace(first_substring, second_substring)


def alteration(substring: str):
    if substring in spell:
        return spell.replace(substring, '')


spell = input()
while True:
    command_list = input().split()
    command = command_list[0]
    if command == "Abracadabra":
        break
    if command == "Abjuration":
        spell = spell.upper()
        print(spell)
    elif command == "Necromancy":
        spell = spell.lower()
        print(spell)
    elif command == "Illusion":
        spell_ = illusion(int(command_list[1]), command_list[2])
        if spell_:
            spell = spell_
            print("Done!")
    elif command == "Divination":
        spell_ = divination(command_list[1], command_list[2])
        if spell_:
            spell = spell_
            print(spell)
    elif command == "Alteration":
        spell_ = alteration(command_list[1])
        if spell_:
            spell = spell_
            print(spell)
    else:
        print("The spell did not work!")