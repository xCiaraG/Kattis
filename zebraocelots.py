n = int(input())
s = ""
for i in range(n):
	if input().strip() == "O":
		s += "1"
	else:
		s += "0"

print(int(s, base=2))