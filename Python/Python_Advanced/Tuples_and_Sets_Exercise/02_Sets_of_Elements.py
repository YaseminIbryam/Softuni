n, m = tuple(map(int, input().split()))
n_set = {int(input()) for _ in range(n)}
m_set = {int(input()) for _ in range(m)}
result = n_set.intersection(m_set)
while result:
    print(result.pop())