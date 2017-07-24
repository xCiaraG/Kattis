import sys
numbers = list(map(int, sys.stdin.readline().strip().split()))
d = {}
for i in range(0, numbers[0]):
    line = sys.stdin.readline().strip().split()
    d[line[0]] = int(line[1])

for i in range(0, numbers[1]):
    line = sys.stdin.readline().strip().split()
    count = 0
    while line != ["."]:
        for word in line:
            if word in d:
                count += d[word]
        line = sys.stdin.readline().strip().split()
    print(count)
