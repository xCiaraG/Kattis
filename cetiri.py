import sys
line = list(map(int, sys.stdin.readline().strip().split()))
line = sorted(line)
if line[1] - line[0] > line[2] - line[1]:
    print(line[0] + (line[1] - line[0])//2)
elif line[1] - line[0] == line[2] - line[1]:
    print(line[2] + line[2]-line[1])
else:
    print(line[1] + (line[2] - line[1])//2)
