import math
n = int(input())
coordinates = []
def distance(x1, y1, x2, y2):
    return math.sqrt((x2-x1)**2+(y2-y1)**2)
for i in range(0, n):
    line = list(map(float, input().strip().split()))
    coordinates.append((line, i))

prev = coordinates[0]
coordinates.remove(coordinates[0])
print(0)
while coordinates:
    m = distance(prev[0][0], prev[0][1], coordinates[0][0][0], coordinates[0][0][1])
    m_i = coordinates[0][1]
    r = coordinates[0]
    for points in coordinates:
        if distance(prev[0][0], prev[0][1], points[0][0], points[0][1]) < m:
            m = distance(prev[0][0], prev[0][1], points[0][0], points[0][1])
            m_i = points[1]
            r = points
    prev = r
    coordinates.remove(r)
    print(m_i)
