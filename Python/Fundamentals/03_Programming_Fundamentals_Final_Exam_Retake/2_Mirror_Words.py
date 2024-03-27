import re

text = input()
pattern = r"(\@|\#)([a-zA-Z]{3,})\1{2}([a-zA-Z]{3,})\1"
pairs = re.findall(pattern, text)
mirror_words = []
if pairs:
    print(f"{len(pairs)} word pairs found!")
    for pair in pairs:
        word_1, word_2 = pair[1:]
        if word_1 == word_2[::-1]:
            mirror_words.append(f'{word_1} <=> {word_2}')
else:
    print("No word pairs found!")
if mirror_words:
    print("The mirror words are:")
    print(', '.join(mirror_words))
else:
    print("No mirror words!")
