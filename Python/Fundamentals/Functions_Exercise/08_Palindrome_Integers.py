def find_is_palindrome(number):  # number have to be string
    for i in range(len(str(number)) // 2):
        if number[i] != number[-i - 1]:
            return False
    return True


for num in input().split(", "):
    print(find_is_palindrome(num))
