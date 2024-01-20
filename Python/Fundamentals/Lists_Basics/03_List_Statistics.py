lines = int(input())
positive = []
negative = []
for line in range(lines):
    number = int(input())
    if number >= 0:
        positive.append(number)
    else:
        negative.append(number)
print(positive)
print(negative)
print("Count of positives:", len(positive))
print("Sum of negatives:", sum(negative))
