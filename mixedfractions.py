import sys
line = list(map(int, sys.stdin.readline().strip().split()))
while line != [0,0]:
    print("{} {} / {}".format(line[0]//line[1], line[0]%line[1], line[1]))
    line = list(map(int, sys.stdin.readline().strip().split()))
