clothes = [int(i) for i in input().split()]
capacity_per_rack = int(input())
sum_cloth = 0
racks = 1
while clothes:
    value = clothes.pop()
    sum_cloth += value
    if sum_cloth == capacity_per_rack and clothes:
        sum_cloth = 0
        racks += 1
    elif sum_cloth > capacity_per_rack:
        sum_cloth = value
        racks += 1
print(racks)



