from sys import stdin
t, average = [int(x) for x in stdin.readline().split()]
results = [int(x) for x in stdin.readline().split()]
count = 0
if average == 100:
	print("impossible")
else:
	while sum(results) // t < average:
		t += 1
		count += 1
		results.append(100)
	print(count)