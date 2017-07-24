import sys
n = int(sys.stdin.readline().strip())
n = bin(n)
n = n[2:]
n = n[::-1]
n = int(n, 2)
print(n)
