from sys import stdin
n, h, v = [int(x) for x in stdin.readline().split()]
print(max(h*v*4,(n-h)*(n-v)*4,(n-h)*v*4,h*(n-v)*4))