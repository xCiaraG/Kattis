from sys import stdin
n = input()
for i in range(0, n):
	line = stdin.readline()
	a, b = [float(x) for x in stdin.readline().split()]
	computers = [int(x) for x in stdin.readline().split()]
	economics = [int(x) for x in stdin.readline().split()]
	avg_computer = sum(computers)/a
	avg_economics = sum(economics)/b
	c = 0
	for student in computers:
		if avg_economics < student < avg_computer:
			c += 1
	print(c)
	
