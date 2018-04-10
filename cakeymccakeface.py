from collections import defaultdict
from sys import stdin
n = int(stdin.readline())
m = int(stdin.readline())
cake_in = [int(x) for x in stdin.readline().split()]
cake_out = [int(x) for x in stdin.readline().split()]
cooking_time = defaultdict(int)
for c1 in cake_in:
	for c2 in cake_out:
		if c2 - c1 >= 0:
			cooking_time[c2 - c1] += 1

ans_time = 0
cakes = 0
for time in sorted(cooking_time):
	if cooking_time[time] > cakes:
		cakes = cooking_time[time]
		ans_time = time

print(ans_time)