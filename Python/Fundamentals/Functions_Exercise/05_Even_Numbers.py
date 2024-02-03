def is_even(number):
    if number % 2 == 0:
        return True
    else:
        return False


print(list(filter(is_even, list(map(int, input().split())))))
