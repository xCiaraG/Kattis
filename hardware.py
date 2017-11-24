n = int(input())
for i in range(n):
	d, count = {"0":0, "1":0, "2":0, "3":0, "4":0, "5":0, "6":0, "7":0, "8":0, "9":0}, 0
	line1 = input()
	line2 = input()
	m = int(line2.split()[0])
	while count != m:
		line = input().split()
		if line[0] == "+":
			for i in range(int(line[1]), int(line[2])+1, int(line[3])):
				count += 1
				for digit in str(i):
					d[digit] += 1
		else:
			count += 1
			for digit in line[0]:
				d[digit] += 1
	print(line1)
	print(line2)
	total = 0
	for i in range(10):
		print("Make {} digit {}".format(d[str(i)], i))
		total += d[str(i)]
	if total > 1:
		print("In total {} digits".format(total))
	else:
		print("In total 1 digit")


