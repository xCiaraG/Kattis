n = int(input().strip())
for i in range(0, n):
    line = list(map(int, input().strip().split()))
    numbers_keys = line[1]
    presses = sorted(list(map(int, input().strip().split())), reverse=True)
    total = 0
    p = 1
    j = 0
    while j*numbers_keys < len(presses):
        total += p*(sum(presses[j*numbers_keys:(j*numbers_keys)+numbers_keys]))
        j += 1
        p += 1
    print("Case #{}: {}".format(i+1, total))