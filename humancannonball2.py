import sys, math
n = int(sys.stdin.readline().strip())
for i in range(0,n):
    line = list(map(float, sys.stdin.readline().strip().split()))
    t = line[2]/(line[0]*math.cos(math.radians(line[1])))
    y = (line[0]*t*math.sin(math.radians(line[1]))) - (.5*9.81*(t**2))
    if y <= line[4] - 1 and y >= line[3] + 1:
        print("Safe")
    else:
        print("Not Safe")
