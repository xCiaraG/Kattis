n = int(input())
t = 0
for i in range(0, n):
	if "CD" not in input().strip():
		t += 1
print(t)