def test(experiments):
	bacteria = 1
	for num in experiments:
		bacteria *= 2 
		bacteria -= num
		if bacteria < 0:
			return "error"
	return bacteria % (10**9 + 7)

n = int(input())
experiments = [int(x) for x in input().split()]
print(test(experiments))