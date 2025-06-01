names_count = int(input())
names = [input() for name in range(names_count)]
print('\n'.join([name for name in set(names)]))