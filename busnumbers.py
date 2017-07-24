n = int(input())
bus_numbers = sorted(list(map(int, input().strip().split())))
i = 1
a = []
prev = bus_numbers[0]
tmp = [prev]
for number in bus_numbers[1:]:
	if number == tmp[-1] + 1:
		tmp.append(number)
	else:
		a.append(tmp)
		tmp = [number]
a.append(tmp)
s = ""
for l in a:
	if len(l) == 1:
		s += str(l[0]) + " "
	elif len(l) == 2:
		s += str(l[0]) + " " + str(l[1]) + " "
	else:
		s += str(l[0]) + "-" + str(l[-1]) + " "

print(s.strip())