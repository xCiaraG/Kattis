import sys
d ={}
tmp = []
numbers = list(map(int,sys.stdin.readline().strip().split()))
line = sys.stdin.readline().strip()
for c in line:
    tmp.append(c)
new_numbers = numbers[:]
numbers.sort()
tmp.sort()
i = 0
while i < len(tmp):
    d[tmp[i]] = numbers[i]
    i += 1
line2 = ""
for c in line:
    line2 += str(d[c]) + " "
print(line2.strip())

