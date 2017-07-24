import sys
line = list(map(int, sys.stdin.readline().strip().split()))
space1 = line[1]-line[0]-1
space2 = line[2]-line[1]-1
if space2> space1:
    print(space2)
else:
    print(space1)
