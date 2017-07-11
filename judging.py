n = int(input().strip())
kattis = {}
domjudge = {}

for i in range(0, n):
	tmp = input().strip()
	if tmp in kattis:
		kattis[tmp] += 1
	else:
		kattis[tmp] = 1

for i in range(0, n):
	tmp = input().strip()
	if tmp in domjudge:
		domjudge[tmp] += 1
	else:
		domjudge[tmp] = 1

total = 0
for result in set(kattis): 
	if result in kattis and result in domjudge:
		total += min(kattis[result], domjudge[result])

print(total)