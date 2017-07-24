import math

def distance(x1, y1, x2, y2):
    return(math.sqrt((x2-x1)**2 + (y2-y1)**2))

a = list(map(int, input().strip().split()))
b = list(map(int, input().strip().split()))
c = list(map(int, input().strip().split()))
d = distance(a[0], a[1], b[0], b[1])
x, y, z = a, b, c
if distance(b[0], b[1], c[0], c[1]) > d:
    x, y, z = b, c, a
if distance(c[0], c[1], a[0], a[1]) > d:
    x, y, z = a, c, b
mid = [(x[0]+y[0])/2,(x[1]+y[1])/2]
new = [(mid[0]*2)-z[0], (mid[1]*2)-z[1]]
print(*(list(map(int, new))))