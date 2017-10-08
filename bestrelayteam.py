n = int(input())
first = []
rest = []
for i in range(n):
	tmp = input().split()
	first.append((float(tmp[1]), tmp[0]))
	rest.append((float(tmp[2]), tmp[0]))

first = sorted(first)[:4]
rest = sorted(rest)[:4]
attempts = []

for time, person in first:
	people = [person]
	i = 0
	while len(people) != 4:
		if rest[i][1] != person:
			people.append(rest[i][1])
			time += rest[i][0]
		i += 1
	attempts.append((time, people))

attempts = sorted(attempts)
print(attempts[0][0])
for person in attempts[0][1]:
	print(person)


