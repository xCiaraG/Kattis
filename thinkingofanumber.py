from sys import stdin
n = int(stdin.readline())
while n != 0:
	minimum = 1
	maximum = 50001
	divisors = []
	ans = []
	for i in range(0, n):
		tmp = stdin.readline().split()
		if tmp[0] == "less" and int(tmp[-1]) < maximum:
			maximum = int(tmp[-1]) 
		elif tmp[0] == "greater" and int(tmp[-1]) + 1 > minimum:
			minimum = int(tmp[-1]) + 1
		elif tmp[0] == "divisible":
			divisors.append(int(tmp[-1]))
	if maximum == 50001:
		print("infinite")
	else:
		if divisors:
			t = max(divisors)
			divisors.remove(max(divisors))
			if minimum % t != 0:
				minimum += (t - (minimum % t))
			for i in range(minimum, maximum, t):
				ans.append(i)
		else:
			ans = [i for i in range(minimum, maximum)]
		for d in divisors:
			j = 0
			while j < len(ans):
				if ans[j] % d != 0:
					ans.remove(ans[j])
				else:
					j += 1
		if ans:
			print(" ".join(map(str, ans)))
		else:
			print("none")
	n = int(stdin.readline())