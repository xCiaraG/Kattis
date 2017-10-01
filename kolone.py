line = input()
left = [(l, "left") for l in list(input().strip())[::-1]]
right = [(l, "right") for l in list(input().strip())]
ants = left + right
for i in range(0, int(input())):
	j = 0
	while j < len(ants) - 1:
		if ants[j][1] == "left" and ants[j+1][1] == "right":
			ants[j], ants[j+1] = ants[j+1], ants[j]
			j += 1
		j += 1
ans = ""
for l, p in ants:
	ans += l
print(ans)