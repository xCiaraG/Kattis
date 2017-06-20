n = int(input())
maxil = [0]*n
minir = [0]*n
array = list(map(int, input().strip().split()))
maxi = array[0]
mini = array[-1]
i = 0
while i < n:
	if array[i] > maxi:
		maxi = array[i]
	if array[n-i-1] < mini:
		mini = array[n-i-1]
	maxil[i] = maxi
	minir[n-i-1] = mini
	i += 1
count = 0
i = 0
while i < n:
	if array[i] >= maxil[i] and array[i] <= minir[i]:
		count += 1
	i += 1

print(count)