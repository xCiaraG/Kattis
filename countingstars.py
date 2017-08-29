from sys import stdin
import heapq

def go(x, y, sky):
    to_go = []
    heapq.heappush(to_go, (x, y))
    while to_go:
        pos = heapq.heappop(to_go)
        x, y = pos[0], pos[1]
        if x >= 0 and y >= 0 and x < len(sky) and y < len(sky[x]) and sky[x][y] != "#":
            sky[x][y] = "#"
            heapq.heappush(to_go, (x-1, y))
            heapq.heappush(to_go, (x+1, y))
            heapq.heappush(to_go, (x, y-1))
            heapq.heappush(to_go, (x, y+1))
    return sky

lines = stdin.readlines()
i = 0
t = 1
while i < len(lines):
    sky = []
    line = [int(x) for x in lines[i].split()]
    r = line[0]
    c = line[1]
    for j in range(1, r+1): 
        sky.append([x for x in lines[i+j].strip()])
    i += line[0] + 1
    count = 0
    for a in range(0, r):
        for b in range(0, c):
            if sky[a][b] == "-":
                count += 1
                sky[a][b] = "#"
                sky = go(a-1, b, sky)
                sky = go(a+1, b, sky)
                sky = go(a, b-1, sky)
                sky = go(a, b+1, sky)
    print("Case {}: {}".format(t, count))
    t += 1