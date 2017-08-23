from sys import stdin
import heapq

def go(x, y):
    to_go = []
    heapq.heappush(to_go, (x, y))
    while to_go:
        pos = heapq.heappop(to_go)
        x, y = pos[0], pos[1]
        if binary_map[x][y] == case:
            binary_map[x][y] = other
            if x > 0 and binary_map[x-1][y] == case:
                heapq.heappush(to_go, (x-1, y))
            if y > 0 and binary_map[x][y-1] == case:
                heapq.heappush(to_go, (x, y-1))
            if y < l2 - 1 and binary_map[x][y+1] == case:
                heapq.heappush(to_go, (x, y+1))
            if x < l1 - 1 and binary_map[x+1][y] == case:
                heapq.heappush(to_go, (x+1, y))

def check(x, y):
    if x == y:
        if d[x] == "1":
            print "decimal"
        else:
            print "binary"
    else:
        print "neither"

l1, l2 = [int(x) for x in stdin.readline().split()]
binary_map = [0]*l1
for i in range(0, l1):
    line = list(stdin.readline().strip())
    binary_map[i] = line
other = 0
d = {}
m = int(stdin.readline())

for i in range(0, m):
    x1, y1, x2, y2 = [int(x) - 1 for x in stdin.readline().split()]
    tmp1 = binary_map[x1][y1]
    tmp2 = binary_map[x2][y2]
    if type(tmp1) == int or type(tmp2) == int or tmp1 != tmp2:
        check(tmp1, tmp2)
    else:
        other += 1
        case = tmp1
        d[other] = case
        go(x1, y1)
        check(binary_map[x1][y1], binary_map[x2][y2])