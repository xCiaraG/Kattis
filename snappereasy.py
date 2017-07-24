import sys
n = int(sys.stdin.readline().strip())
for i in range(0,n):
	line = list(map(int,sys.stdin.readline().strip().split()))
	'''
	chain = [0]*line[0]
	for j in range(0, line[1]):
		k = 0
		prev = 1
		while k < len(chain) and prev == 1 :
			prev = chain[k]
			if chain[k]:
				chain[k] = 0
			else:
				chain[k] = 1
			k += 1
			print(chain)
			if sum(chain) == len(chain):
				print(j, "hi")
	if sum(chain) != len(chain):
		print("Case #{}: OFF".format(i+1))
	else:
		print("Case #{}: ON".format(i+1))
	'''
	d = 2**line[0]
	if (line[1] - (d-2)) -1 == 0 or (line[1]-(d-2)-1) % d == 0:
		print("Case #{}: ON".format(i+1))
	else:
		print("Case #{}: OFF".format(i+1))