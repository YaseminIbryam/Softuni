n = int(input())
for i in range(n):
    string = input()
    is_pure = True
    for char in string:
        if char == "," or char == "." or char == "_":
            is_pure = False
    if is_pure:
        print(f"{string} is pure.")
    else:
        print(f"{string} is not pure!")

