from sys import stdin
n = int(stdin.readline())
total = 0
for _ in range(n):
	colour = "".join(x.lower() for x in stdin.readline())
	if "pink" in colour or "rose" in colour:
		total += 1
if total:
	print(total)
else:
	print("I must watch Star Wars with my daughter")