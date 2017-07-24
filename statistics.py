import sys
lines = sys.stdin.readlines()
i = 1
for line in lines:
    line = list(map(int,line.strip().split()))
    line.remove(line[0])
    line = sorted(line)
    print("Case {}: {} {} {}".format(i, line[0], line[len(line)-1], line[len(line)-1]-line[0]))
    i += 1
