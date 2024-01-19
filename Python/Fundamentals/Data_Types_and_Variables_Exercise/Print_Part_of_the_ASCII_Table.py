# start = int(input())
# stop = int(input())
# for index in range(start, stop + 1):
#     print(chr(index), end=' ')
print(*[chr(index) for index in range(int(input()), (int(input()) + 1))], end=' ')