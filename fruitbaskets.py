from math import factorial
from itertools import combinations
from sys import stdin

def combins(n, r):
	return (factorial(n)) // ((factorial(r)) * (factorial(n-r)))

n = int(stdin.readline())
fruit = [int(x) for x in stdin.readline().split()]
total = 0

i = 1
while i < 4 and i <= n:
	for c in combinations(fruit, i):
		if sum(c) >= 200:
			total += sum(c)
	i += 1
for i in range(4, n + 1):
	tmp = combins(n-1, i-1)
	for f in fruit:
		total += tmp*f
print(total)