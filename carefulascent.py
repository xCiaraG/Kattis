coordinates = [int(x) for x in input().split()]
y = coordinates[1]
t = 0
n = int(input())
for i in range(0, n):
	shield = [float(x) for x in input().split()]
	t += (shield[1] - shield[0])*shield[2]
	y -= (shield[1] - shield[0])
t += y
print(coordinates[0]/t)