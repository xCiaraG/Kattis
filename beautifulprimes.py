from sys import stdin
n = int(stdin.readline())
for _ in range(n):
	t11, t3 = 0, 0
	m = int(stdin.readline())
	t11 = m 
	while len(str((11**t11) * (3**t3))) != m:
		t11 -= 1
		t3 += 1
	print(" ".join((["3"] * t3) + (["11"] * t11))) 