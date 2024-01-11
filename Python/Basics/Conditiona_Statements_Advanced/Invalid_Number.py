number = int(input())
is_valid = True
if 100 <= number <= 200 or number == 0:
    is_valid = True
else:
    is_valid = False
if not is_valid:
    print("invalid")
