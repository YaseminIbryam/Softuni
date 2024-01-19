lines = int(input())
is_balanced = True
is_bracket_opened = False
for line in range(lines):
    string = input()
    if string == '(' or string == ')':
        if is_bracket_opened:
            if string == '(':
                is_balanced = False
                break
            elif string == ')':
                is_bracket_opened = False
        elif string == '(':
            is_bracket_opened = True
        elif string == ')':
            is_balanced = False
            break
if is_balanced:
    print("BALANCED")
else:
    print("UNBALANCED")

# number = int(input())
# counter = 0
# for _ in range(number):
#     check = input()
#     if "(" in check:
#         counter += 1
#     elif ")" in check:
#         counter -= 1
#     if 0 != counter != 1:
#         print("UNBALANCED")
#         break
# else:
#     print("BALANCED")
