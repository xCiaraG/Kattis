n = int(input().strip())
for i in range(0, n):
    line = list(map(int, input().strip().split()))
    island = line[1:]
    count = 0
    j = 1
    while j < len(island):
        k = j + 1
        while k < len(island):
            tmp = island[j:k]
            if min(tmp) > island[j-1] and min(tmp) > island[k]:
                count += 1
            k += 1
        j += 1
    print(line[0], count)