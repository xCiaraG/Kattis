n = int(input())
for i in range(n):
	b, p = [float(x) for x in input().split()]
	bpm = 60*b/p
	print("{} {} {}".format(bpm - 60/p, bpm, bpm + 60/p))