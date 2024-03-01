words_and_synonyms = {}
for i in range(int(input())):
    word, synonym = input(), input()
    if word not in words_and_synonyms:
        words_and_synonyms[word] = [synonym]
    else:
        words_and_synonyms[word].append(synonym)
for word, synonyms in words_and_synonyms.items():
    print(f"{word} - {', '.join(synonyms)}")