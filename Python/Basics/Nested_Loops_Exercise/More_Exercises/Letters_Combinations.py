alphabet = 'abcdefghijklmnopqrstuvwxyz'
count = 0
start_letter = input()
end_letter = input()
exclude_letter = input()
start_index = alphabet.index(start_letter)
end_index = alphabet.index(end_letter)
for first in range(start_index, end_index + 1):
    if alphabet[first] == exclude_letter:
        continue
    for second in range(start_index, end_index + 1):
        if alphabet[second] == exclude_letter:
            continue
        for third in range(start_index, end_index + 1):
            if alphabet[third] == exclude_letter:
                continue
            print(alphabet[first] + alphabet[second] + alphabet[third], end=' ')
            count += 1
print(count)

