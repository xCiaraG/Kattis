n = int(input())
for i in range(n):
	results = [int(x) for x in input().split()]
	average = sum(results[1:])/results[0]
	t = 0
	for student in results[1:]:
		if student > average:
			t += 1
	print("{:.3f}%".format(t/results[0]*100))