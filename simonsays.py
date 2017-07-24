import sys
n = int(sys.stdin.readline().strip())
for i in range(0,n):
    line = sys.stdin.readline().strip().split()
    if line[0] == "Simon" and line[1] == "says":
        print(" ".join(line[2:]))
