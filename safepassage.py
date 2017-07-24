n = list(map(int, input().strip().split()))
n.remove(n[0])
times = sorted(n)
time = 0
while times:
	if len(times) == 2:
		time += times[1]
		times = []
	elif len(times) == 3:
		time += sum(times)
		times = []
	elif times[1] > times[-1]//2:
		time += times[-1] + times[-2] + times[0]*2
		times.pop()
		times.pop()
	else:
		time += times[1]*2 + times[0] + times[-1]
		times.pop()
		times.pop()
print(time)