n = int(input())
if n % 2 == 0:
	n += 2
	n = n//2
	n = n**2
else:
	n += 3
	n = n//2
	n = n**2 - n
print(n)