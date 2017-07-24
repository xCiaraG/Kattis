n = int(input().strip())
while n != 0:
    coordinates = []
    for i in range(0, n):
        coordinate = list(map(int, input().strip().split()))
        coordinates.append(coordinate)
    coordinates.append(coordinates[0])
    j, x, y = 0, 0, 0
    while j + 1 < len(coordinates):
        x += (coordinates[j][0]*coordinates[j+1][1])
        y += (coordinates[j][1]*coordinates[j+1][0])
        j += 1
    ans = .5*(y-x)
    if ans > 0:
        d = "CW"
    else:
        ans = abs(ans)
        d = "CCW"
    print(d, ans)
    n = int(input().strip())
