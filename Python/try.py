numbers = [2, 4, 6, 8, 10]
result = [i for i in numbers if all(i % j != 0 for j in range(2, i))]
print(result)

nums = [-1 ,  -2 ]
for i in nums:
    if i % 2 == 0:
        print(i)