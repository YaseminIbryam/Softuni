N = int(input())
odds = set()
evens = set()
for row in range(1, N + 1):
    name = input()
    ascii_sum = sum([ord(char) for char in name]) // row
    if ascii_sum % 2 == 0:
        evens.add(ascii_sum)
    else:
        odds.add(ascii_sum)
sum_evens = sum(evens)
sum_odds = sum(odds)
if sum_evens == sum_odds:
    result = odds.union(evens)
elif sum_odds > sum_evens:
    result = odds.difference(evens)
else:
    result = odds.symmetric_difference(evens)
print(', '.join(map(str, result)))







