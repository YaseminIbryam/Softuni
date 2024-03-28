def cast_spell(name: str, MP_needed: int, spell_name: str):
    if heroes[name]['MP'] >= MP_needed:
        heroes[name]['MP'] -= MP_needed
        print(f"{name} has successfully cast {spell_name} and now has {heroes[name]['MP']} MP!")
    else:
        print(f"{name} does not have enough MP to cast {spell_name}!")


def take_damage(name: str, damage: int, attacker: str):
    heroes[name]['HP'] -= damage
    if heroes[name]['HP'] > 0:
        print(f"{name} was hit for {damage} HP by {attacker} and now has {heroes[name]['HP']} HP left!")
    else:
        del heroes[name]
        print(f"{name} has been killed by {attacker}!")


def recharge(name: str, amount: int):
    MP = heroes[name]['MP']
    heroes[name]['MP'] += amount
    if heroes[name]['MP'] > 200:
        heroes[name]['MP'] = 200
    print(f"{name} recharged for {heroes[name]['MP'] - MP} MP!")


def heal(name: str, amount: int):
    HP = heroes[name]['HP']
    heroes[name]['HP'] += amount
    if heroes[name]['HP'] > 100:
        heroes[name]['HP'] = 100
    print(f"{name} healed for {heroes[name]['HP'] - HP} HP!")


n = int(input())
heroes = {}
for i in range(n):
    hero_name, HP, MP = input().split()
    heroes[hero_name] = {'HP': int(HP), 'MP': int(MP)}
while True:
    command_list = input().split(' - ')
    command = command_list[0]
    if command == 'End':
        break
    hero_name = command_list[1]
    if command == 'CastSpell':
        cast_spell(hero_name, int(command_list[2]), command_list[3])
    elif command == 'TakeDamage':
        take_damage(hero_name, int(command_list[2]), command_list[3])
    elif command == 'Recharge':
        recharge(hero_name, int(command_list[2]))
    elif command == 'Heal':
        heal(hero_name, int(command_list[2]))
for hero, points in heroes.items():
    print(hero)
    print(f"HP: {points['HP']}")
    print(f"MP: {points['MP']}")
