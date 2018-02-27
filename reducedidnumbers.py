from sys import stdin
sins = []
n = int(stdin.readline())
for i in range(n):
	sins.append(int(stdin.readline()))
current = 1
while len(set([x % current for x in sins])) != n:
	current += 1
print(current)