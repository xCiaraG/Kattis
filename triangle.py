import sys
nums = sys.stdin.readlines()
i = 1
for n in nums:
	n = int(n.strip())
	ans = len(str((3**(n+1))//(2**n)))
	print("Case {}: {}".format(i, ans))
	i += 1
