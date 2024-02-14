def palindrome(word):
    if word == word[::-1]:
        return word


words = input().split()
palindromes = [word for word in words if palindrome(word)]
palindromes_count = palindromes.count(input())
print(palindromes)
print(f"Found palindrome {palindromes_count} times")