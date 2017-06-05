import sys
lines = sys.stdin.readlines()
i = 0
count = 0
while i < len(lines):
	line = lines[i].strip()
	if line == "OPEN" and i != 0:
		print()
	if line == "OPEN":
		count += 1
		customers_fees = []
		customer_time = {}
		c = []
	elif line == "CLOSE":
		print("Day {}".format(count))
		customers_fees = sorted(customers_fees)
		for customer in customers_fees:
			print("{} ${:.2f}".format(customer[0], customer[1]))
	else:
		line = line.split()
		if line[0] == "ENTER":
			customer_time[line[1]] = int(line[2])
		else:
			time = int(line[2]) - customer_time[line[1]]
			price = time * .1
			if line[1] in c:
				k = 0
				while k < len(customers_fees):
					if customers_fees[k][0] == line[1]:
						price = price + customers_fees[k][1]
						customers_fees[k] = (line[1], price)
					k += 1
			else:
				customers_fees.append((line[1], price))
				c.append(line[1])
	i += 1