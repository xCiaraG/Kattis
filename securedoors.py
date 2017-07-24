import sys
n = int(sys.stdin.readline().strip())
d = {}
for i in range(0, n):
    line = sys.stdin.readline().strip().split()
    if line[1] not in d:
        d[line[1]] = "exit"
    if d[line[1]] != line[0] and line[0] == "entry":
        print(line[1], "entered")
        d[line[1]] = line[0]
    elif d[line[1]] != line[0] and line[0] == "exit":
        print(line[1], "exited")
        d[line[1]] = line[0]
    elif d[line[1]] == "exit":
        print(line[1], "exited (ANOMALY)")
    else:
        print(line[1], "entered (ANOMALY)")
