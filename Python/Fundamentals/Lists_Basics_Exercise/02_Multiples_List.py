factor = int(input())
# print([factor * multiplier for multiplier in range(1, int(input()) + 1)])
result_list = []
count = int(input())
for multiplier in range(1, count + 1):
    result_list.append(factor * multiplier)
print(result_list)