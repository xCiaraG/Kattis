import sys
n = int(sys.stdin.readline().strip())
for i in range(0,n):
    line = sys.stdin.readline().strip().split()
    if len(line) > 1 and line[0] == "simon" and line[1] == "says":
        print(" ".join(line[2:]))
    else:
        print()
