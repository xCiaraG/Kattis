import sys
lines = sys.stdin.readlines()
words = []
for line in lines:
    line = line.strip().split()
    for word in line:
        words.append(word)

compound_words = []
for word in words:
    for other_word in words:
        if word != other_word:
            compound_words.append(word + other_word)

compound_words = sorted(set(compound_words))

for word in compound_words:
    print(word)
