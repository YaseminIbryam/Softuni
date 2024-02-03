def odd_and_even_sum(number):
    even_sum = sum([int(num) for num in number if int(num) % 2 == 0])
    odd_sum = sum([int(num) for num in number if int(num) % 2 != 0])
    return even_sum, odd_sum


even_sum, odd_sum = odd_and_even_sum(input())

print(f"Odd sum = {odd_sum}, Even sum = {even_sum}")
