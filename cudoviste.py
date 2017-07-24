n = list(map(int, input().strip().split()))
h = n[0]
w = n[1]
parking = []
for i in range(0, h):
    line = input().strip()
    l = []
    for c in line:
        l.append(c)
    parking.append(l)

for t in range(0, 5):
    i = 0
    total = 0
    while i < h - 1:
        j = 0
        while j < w - 1:
            X_count = 0
            free = 0
            if parking[i][j] == "X":
                X_count += 1
            elif parking[i][j] == ".":
                free += 1
            if parking[i+1][j] == "X":
                X_count += 1
            elif parking[i+1][j] == ".":
                free += 1
            if parking[i][j+1] == "X":
                X_count += 1
            elif parking[i][j+1] == ".":
                free += 1
            if parking[i+1][j+1] == "X":
                X_count += 1
            elif parking[i+1][j+1] == ".":
                free += 1
            if X_count == t and X_count + free == 4:
                total += 1
            j += 1
        i += 1
    print(total)
