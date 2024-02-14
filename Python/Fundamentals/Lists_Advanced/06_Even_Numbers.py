numbers = list(map(int, input().split(", ")))
indices_of_even_numbers = [index for index, value in enumerate(numbers) if value % 2 == 0]
print(indices_of_even_numbers)
