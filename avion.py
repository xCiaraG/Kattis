from sys import stdin
result = []
for i in range(1, 6):
	if "FBI" in stdin.readline():
		result.append(str(i))
if result: 
	print(" ".join(result))
else:
	print("HE GOT AWAY!")