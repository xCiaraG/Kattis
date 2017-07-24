line = list(map(int, input().strip().split()))
line = line[1:]
test = line
count = 0
tmp1 = []
while sorted(line)[0] != sorted(line)[-1]:
    tmp2 = []
    i = 1
    while i < len(line):
        tmp2.append(line[i]-line[i-1])
        i += 1
    tmp1.append(line[-1])
    line = tmp2
    count += 1
tmp1.append(line[-1])
print(count, sum(tmp1))
