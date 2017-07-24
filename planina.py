n = int(input())
i = 2
j = 3
for k in range(1, n):
    j += i
    i *= 2
print(j**2)
