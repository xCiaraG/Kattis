n = int(input())
while (n-1) % 4 != 0:
	n += 1
print(n)

k = 2
t = 0
for i in range (1, 35):
	t += k
	k += 3
	print(t)
