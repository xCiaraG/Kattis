n = int(input())
c = 1
for i in range(2, 128):
	if n % (i**9) == 0:
		c = i
print(c)
