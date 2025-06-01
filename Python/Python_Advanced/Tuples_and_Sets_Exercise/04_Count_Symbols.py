characters = list(input())
unique_characters_sorted = sorted(list(set(characters)), reverse=True)
while unique_characters_sorted:
    char = unique_characters_sorted.pop()
    print(f'{char}: {characters.count(char)} time/s')


