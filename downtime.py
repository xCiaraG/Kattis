from sys import stdin
line = [int(x) for x in raw_input().split()]
can_handle = line[1]
n = line[0]
t = 0
l = can_handle
servers = [0]* can_handle
for i in range(0, n):
    m = int(stdin.readline())
    if servers[t] <= m:
        servers[t] = m + 1000
        t = (t + 1) % l
    else:
        servers.append(m + 1000)
        servers += [0]*(can_handle - 1)
        t = l + 1
        l += can_handle
        t = t % l
print(l//can_handle)