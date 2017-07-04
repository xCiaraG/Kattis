line = list(map(float, input().strip().split()))
while line != [0.0, 0.0, 0.0]:
    width = line[-1]/2
    x = []
    y = []
    x_cuts = sorted(list(map(float, input().strip().split())))
    y_cuts = sorted(list(map(float, input().strip().split())))
    for n in x_cuts:
        x.append((n-width, n+width))
    for n in y_cuts:
        y.append((n-width, n+width))
    a = True
    b = True
    current = 0
    for n in x:
        if current >= n[0]:
            current = n[1]
        else:
            a = False
    if current < 75:
        a = False
    current = 0
    for n in y:
        if current >= n[0]:
            current = n[1]
        else:
            b = False
    if current < 100:
        b = False
    if a and b:
        print("YES")
    else:
        print("NO")
    line = list(map(float, input().strip().split()))