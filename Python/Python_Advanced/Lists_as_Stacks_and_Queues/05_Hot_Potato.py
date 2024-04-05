from collections import deque

queue = deque(input().split())
n = int(input()) - 1
while len(queue) > 1:
    queue.rotate(-n)
    print(f"Removed {queue.popleft()}")
print(f"Last is {queue.popleft()}")








# from collections import deque
#
# queue = deque(input().split())
# n = int(input())
# count = 1
# while len(queue) > 1:
#     if count == n:
#         count = 1
#         print('Removed', queue.popleft())
#     else:
#         queue.append(queue.popleft())
#         count += 1
# print('Last is', queue.popleft())