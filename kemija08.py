import sys
line = sys.stdin.readline().strip()
s = ""
i = 0
while i < len(line):
    s += line[i]
    if line[i] in "aeiou":
        i += 2
    i += 1
print(s)
