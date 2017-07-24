import sys
word = sys.stdin.readline().strip()
n = int(sys.stdin.readline().strip())
words = [word]
for i in range(0,n):
    line = sys.stdin.readline().strip().split()
    a = False
    for w in line:
        if word.endswith(w):
            a = True
    if a:
        for w in line:
            words.append(w)

n = int(sys.stdin.readline().strip())
for i in range(0,n):
    line = sys.stdin.readline().strip().split()
    a = False
    for word in words:
        if line[len(line)-1].endswith(word):
                    a = True
    if a:
        print("YES")
    else:
        print("NO")
