# solution 1
for i in range(1000):
    if i % 10 == 7:
        print(i)

# solution 2
for i in range(1, 1001, 1):
    if i % 10 == 7:
        print(i)

# solution 3
for i in range(7, 1001, 10):
    print(i)
