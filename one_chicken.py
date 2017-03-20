n = list(map(int, input().strip().split()))
if n[0] <= n[1] and n[1]-n[0] != 1:
	print("Dr. Chaz will have", n[1]-n[0], "pieces of chicken left over!")
elif n[0] <= n[1]:
	print("Dr. Chaz will have", n[1]-n[0], "piece of chicken left over!")
elif n[0]-n[1] != 1:
	print("Dr. Chaz needs", n[0]-n[1], "more pieces of chicken!")
else:
	print("Dr. Chaz needs", n[0]-n[1], "more piece of chicken!")
