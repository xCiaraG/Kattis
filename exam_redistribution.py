n = int(input())
line = list(map(int, input().strip().split()))
tmp = line[:]
m = max(tmp)
tmp.remove(m)
i = 0 
while i < n:
    line[i] = (line[i], i+1)
    i += 1
line = sorted(line, reverse=True)
s = ""
if sum(tmp) < m:
    s = "impossible"
else:
    for room in line:
        s += str(room[1]) + " "
print(s.strip())