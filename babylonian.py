n = int(input())
for i in range(n):
	number = [0 if x == "" else int(x) for x in input().split(",")]
	print(sum([number[-i-1]*(60**i) for i in range(len(number))]))