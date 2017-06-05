n = int(input())
while n != 0:
	count = 0
	for i in range(0, n):
		word = input().strip()
		if i == 0:
			ans = word
		tmp = word.count("aa") + word.count("ee") + word.count("ii") + word.count("oo") + word.count("uu") + word.count("yy")
		if tmp > count:
			count = tmp
			ans = word
	print(ans)
	n = int(input().strip())
