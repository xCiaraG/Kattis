import sys
lines = sys.stdin.readlines()
words = []
for line in lines:
    line = line.strip().split()
    s = ""
    for word in line:
        if word.lower() not in words:
            words.append(word.lower())
            s += word + " "
        else:
            s += ". "
    print(s.strip())
