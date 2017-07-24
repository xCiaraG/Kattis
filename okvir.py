mport sys
line1 = list(map(int, sys.stdin.readline().strip().split()))
line2 = list(map(int, sys.stdin.readline().strip().split()))
words = []
for i in range(0, line1[0]):
    words.append(sys.stdin.readline().strip())
height = line1[0] + line2[0] + line2[3]
width = line1[1] + line2[1] + line2[2]
symbol = "#."
symbol_pos = 2
word_pos = 0
for i in range(0, height):
    s = ""
    j = 0
    while j < line2[1]:
        s += symbol[symbol_pos%len(symbol)]
        symbol_pos += 1
        j += 1
    if i >= line2[0] and word_pos < len(words):
        s += words[word_pos]
        if len(words[word_pos]) % 2 == 1:
            symbol_pos += 1
        word_pos += 1
        j += line1[1]

    while j < width:
        s += symbol[symbol_pos%len(symbol)]
        symbol_pos += 1
        j += 1
    if width % 2 == 0:
        symbol_pos += 1
    print(s)
