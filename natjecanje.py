line = input().strip()
damaged = [int(x) for x in input().split()]
reserve = [int(x) for x in input().split()]

i = 0
while i < len(damaged):
    if damaged[i] in reserve:
        reserve.remove(damaged[i])
        damaged.remove(damaged[i])
    else:
        i += 1

c = 0
for n in damaged:
    if n - 1 in reserve:
        reserve.remove(n-1)
        c += 1
    elif n + 1 in reserve:
        reserve.remove(n+1)
        c += 1
print(len(damaged) - c)

    



