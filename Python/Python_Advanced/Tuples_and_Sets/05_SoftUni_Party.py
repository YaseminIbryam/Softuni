guest_count = int(input())
regular = set()
vip = set()
for _ in range(guest_count):
    code = input()
    if len(code) == 8:
        if code[0].isdigit():
            vip.add(code)
        else:
            regular.add(code)
while True:
    code = input()
    if code == 'END':
        break
    if code in vip:
        vip.discard(code)
    elif code in regular:
        regular.discard(code)
print(len(regular) + len(vip))
vip = sorted(list(vip), reverse=True)
regular = sorted(list(regular), reverse=True)
while vip:
    print(vip.pop())
while regular:
    print(regular.pop())