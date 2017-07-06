def sieve(num, x):
	c = 0
	l = [True]*(num+1)
	i = 2
	length = num+1
	while i < length:
		j = i
		if l[j]:
			j += i
			c += 1
			if c == x:
				return j-i
			while j < length:
				if l[j]:
					l[j] = False
					c += 1
				if c == x:
					return j
				j += i
		i += 1
line = list(map(int, input().strip().split()))
print(sieve(line[0], line[1]))