n = int(input())
for i in range(0, n):
	line = list(map(int, input().strip().split()))
	s = line[0]
	d = line[1]
	a = False
	i = 0
	while not a and i <= s:
		if abs((s-i)-i) == d:
			nums = [s-i, i]
			nums = sorted(nums)
			print(nums[1], nums[0])
			a = True
		i += 1
	if not a:
		print("impossible")
