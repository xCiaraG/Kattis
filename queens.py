n = int(input())
r, c, d1, d2 = [0]*n, [0]*n, [0]*n, [0]*n
for i in range(0, n):
	x, y = [int(j) for j in raw_input().split()]
	r[i], c[i], d1[i], d2[i] = x, y, x+y, x-y

if len(set(r)) == n and len(set(c)) == n and len(set(d1)) == n and len(set(d2)) == n:
	print("CORRECT")
else:
	print("INCORRECT")