n = int(input())
numbers = input().split()
ans = 'makes sense'
for i in range(n):
	if numbers[i] not in [str(i+1), 'mumble']:
		ans = 'something is fishy'
print(ans)