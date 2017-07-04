n = int(input().strip())
while ((n**2 + n) + ((n-1)**2 + (n-1))//2) % 4 != 0:
    n += 1
print(n)