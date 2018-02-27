n = int(input())
teams = {}
universities = {}
for i in range(n):
	team = input().strip()
	if team not in teams:
		teams[team] = [1, i]
		universities[team.split()[0]] = True
	else:
		teams[team][0] += 1

results = sorted([(v, k) for k, v in teams.items()])
c = 0
i = 0
while c < 12:
	if universities[results[i][1].split()[0]]:
		c += 1
		print(results[i][1])
		universities[results[i][1].split()[0]] = False
	i += 1