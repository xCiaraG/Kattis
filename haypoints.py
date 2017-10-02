from sys import stdin
n, m = [int(x) for x in stdin.readline().split()]
d = {}
for i in range(0, n):
    job, salary = stdin.readline().split()
    d[job] = int(salary)

for i in range(0, m):
    line = stdin.readline().split()
    count = 0
    while line != ["."]:
        for word in line:
            if word in d:
                count += d[word]
        line = stdin.readline().split()
    print(count)
