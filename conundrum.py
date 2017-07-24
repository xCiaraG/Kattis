import sys
word = sys.stdin.readline().strip()
c = 0
i = 0
l = []
for i in range(0, len(word), 3):
    if word[i] != "P":
        c += 1
for i in range(1, len(word), 3):
    if word[i] != "E":
        c += 1
for i in range(2, len(word), 3):
    if word[i] != "R":
            c += 1 
print(c)
