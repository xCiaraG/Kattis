forward = ["lea", "mi", "fur", "ch", "yd", "ft", "in", "th"]
backward = ["th", "in", "ft", "yd", "ch", "fur", "mi", "lea"]
d = {"lea": 3, "mi": 8, "fur": 10, "ch": 22, "yd": 3, "ft": 12, "in": 1000}
convert = {"thou": "th", "inch": "in", "foot": "ft", "yard": "yd", 
			"chain": "ch", "furlong": "fur", "mile": "mi", "league": "lea"}
line = input().strip().split()
if line[1] in convert:
	line[1] = convert[line[1]]
if line[3] in convert:
	line[3] = convert[line[3]]
total = int(line[0])
if forward.index(line[1]) < forward.index(line[3]):
	i = forward.index(line[1])
	j = forward.index(line[3])
	while i < j:
		total *= d[forward[i]]
		i += 1
else:
	i = backward.index(line[1])
	j = backward.index(line[3])
	while i < j:
		total /= d[backward[i+1]]
		i += 1
print(total)
