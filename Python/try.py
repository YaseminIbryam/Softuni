from functools import reduce

numbers = [1, 2, 3, 4, 5]
squared = map(lambda x: x**2, numbers)
result = reduce(lambda x, y: x * y, squared)
print(result)
