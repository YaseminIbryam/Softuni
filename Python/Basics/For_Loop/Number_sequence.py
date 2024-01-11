from sys import maxsize
smallest = maxsize
biggest = -maxsize
rows = int(input())
for i in range(rows):
    number = int(input())
    if number > biggest:
        biggest = number
    if number < smallest:
        smallest = number
print(f"Max number: {biggest}")
print(f"Min number: {smallest}")

