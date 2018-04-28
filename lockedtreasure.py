from math import factorial
from sys import stdin
def ncr(n, r):
    return (factorial(n) / ((factorial(r) * (factorial(n - r)))))

n = int(stdin.readline().strip())
for _ in range(n):
    i, j = [int(x) for x in stdin.readline().split()]
    print(ncr(i, j - 1))