import sys
d = {}
line = sys.stdin.readline().strip().split()
while line:
    d[line[1]] = line[0]
    line = sys.stdin.readline().strip().split()

lines = sys.stdin.readlines()
for line in lines:
    line = line.strip()
    if line in d:
        print(d[line])
    else:
        print("eh")
