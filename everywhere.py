import sys
n = int(sys.stdin.readline().strip())
for i in range(0,n):
    m = int(sys.stdin.readline().strip())
    places = []
    for j in range(0,m):
        places.append(sys.stdin.readline().strip())
    places = set(places)
    print(len(places))
