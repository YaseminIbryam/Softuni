# queue = input()
# list_queue = list(queue.split())
# list_queue = [elem.replace(',', '') for elem in list_queue]
# index_wolf = 0
# for index, animal in enumerate(list_queue):
#     if animal == "wolf":
#         index_wolf = index
#         break
# number_place_wolf = len(list_queue) - index_wolf
# if number_place_wolf == 1:
#     print("Please go away and stop eating my sheep")
# else:
#     print(f"Oi! Sheep number {number_place_wolf - 1}! You are about to be eaten by a wolf!")
animals = list(reversed(input().split(', ')))
print('Please go away and stop eating my sheep' if animals[0] == 'wolf' else f'Oi! Sheep number {animals.index("wolf")}! You are about to be eaten by a wolf!')
