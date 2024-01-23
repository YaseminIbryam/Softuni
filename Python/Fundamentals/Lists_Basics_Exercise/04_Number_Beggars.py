list_of_integers = list(map(int, input().split(", ")))
beggars = int(input())
list_of_sums = []
for beggar in range(beggars):
    sum_for_beggar = 0
    for index in range(beggar, len(list_of_integers), beggars):
        sum_for_beggar += list_of_integers[index]
    list_of_sums.append(sum_for_beggar)
print(list_of_sums)