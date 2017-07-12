import sys
lines = sys.stdin.readlines()
i = 0 
while i < len(lines):
    n = int(lines[i])
    line = lines[i+1].strip()
    for j in range(0,n):
        s = ""
        for c in line:
            if 33 <= ord(c) <= 42 or 91 <= ord(c) <= 93:
                s += str(chr(92)) + c
            else:
                s += c
        line = s
    print(line)
    i += 2