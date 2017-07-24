import sys
pos = list(map(int, sys.stdin.readline().strip().split()))
lines = []
words = []
for i in range(0, int(pos[0])):
    line = sys.stdin.readline().strip()
    word = line
    if "#" not in line:
        words.append(line)
    else:
        w = word.split("#")
        for wo in w:
            if len(wo) > 1:
                words.append(wo)
    lines.append(line)

tmp_words = []
for c in lines[0]:
    tmp_words.append(c)

for j in range(1, len(lines)):
    for i in range (0, len(lines[j])):
        tmp_words[i] += lines[j][i]

for word in tmp_words:
    if "#" not in word:
        words.append(word)
    else:
        w = word.split("#")
        for wo in w:
            if len(wo) > 1:
                words.append(wo)


words = sorted(words)
print(words[0])

