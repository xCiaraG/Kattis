line = list(map(int, input().strip().split()))
to_fill = line[0]
bottle1 = line[1]
bottle2 = line[2]
i = 0
a = True
while a and i*bottle2 <= to_fill:
    if (to_fill - (bottle2 * i)) % bottle1 == 0:
        a = False
    i += 1

if not a:
    print((to_fill - (bottle2 * (i-1))) // bottle1, i - 1)
else:
    print("Impossible")
