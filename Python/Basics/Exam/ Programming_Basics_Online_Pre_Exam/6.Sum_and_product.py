n = int(input())
number = ""
number_found = False
for a in range(1, 10):
    for b in range(9, a - 1, -1):
        for c in range(9):
            for d in range(9, c - 1, -1):
                if a+b+c+d == a*b*c*d and n % 10 == 5:
                    number = f"{a}{b}{c}{d}"
                    number_found = True
                    break
                elif a*b*c*d // (a+b+c+d) == 3 and n % 3 == 0:
                    number = f"{d}{c}{b}{a}"
                    number_found = True
                    break
                else:
                    number = "Nothing found"
            if number_found:
                break
        if number_found:
            break
    if number_found:
        break

print(number)
