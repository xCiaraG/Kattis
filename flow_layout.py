width = int(input().strip())
while width != 0:
    layout = [[width, 0]]
    rectangle = list(map(int, input().strip().split()))
    while rectangle != [-1, -1]:
        if layout[-1][0] - rectangle[0] >= 0:
            if layout[-1][1] < rectangle[1]:
                layout[-1][1] = rectangle[1]
            layout[-1][0] -= rectangle[0]
        else:
            layout.append([width - rectangle[0], rectangle[1]])
        rectangle = list(map(int, input().strip().split()))
    t, m = 0, 0
    for item in layout:
        if width - item[0] > m:
            m = width - item[0]
        t += item[1]
    print("{} x {}".format(m, t))
    width = int(input().strip())