n = int(input())
alice = 0
bob = 0
pieces = sorted([int(x) for x in input().split()], reverse=True)
for i in range(n):
	if i % 2 == 0:
		alice += pieces[i]
	else:
		bob	+= pieces[i]
print(alice, bob)
