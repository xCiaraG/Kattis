from sys import stdin
n = int(stdin.readline())
sequence = [int(x) for x in stdin.readline().split()]
current = sequence[0]
new = [current]
for d in sequence[1:]:
	if d > current:
		current = d
		new.append(current)
print(len(new))
print(*new)