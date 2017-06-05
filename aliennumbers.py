def to_decimal(number, system):
	b = len(system)
	number = number[::-1]
	total = 0
	i = 0
	while i < len(number):
		total += (b**i)*(system.index(number[i]))
		i += 1
	return total

def to_system(number, system):
	b = len(system)
	s = ""
	i = 0
	while b**i <= number:
		i += 1
	i -= 1
	while i >= 0:
		tmp = number//b**i
		s += system[tmp]
		number = number % b**i
		i -= 1
	return s

n = int(input())
for i in range(0, n):
	line = input().strip().split()
	number = to_decimal(line[0], line[1])
	print("Case #{}: {}".format(i+1,to_system(number, line[2])))