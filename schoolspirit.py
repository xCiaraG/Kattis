from sys import stdin

def score(l):
	total = 0
	for i in range(len(l)):
		total += l[i]*(0.8**i)
	return total*.2

n = int(stdin.readline())
scores = [int(x) for x in stdin.readlines()]
total = 0
for i in range(n):
	total += score(scores[:i] + scores[i+1:])
print(score(scores))
print(total/n)
