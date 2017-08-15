from copy import deepcopy
from sys import stdin
n = int(input())
tax_bands = []
for i in range(0, n):
	tax_bands.append([float(x) for x in stdin.readline().split()])
final_tax = float(input())
n = int(input())
for i in range(0, n):
	earned, to_give = [float(x) for x in stdin.readline().split()]
	total = 0
	tmp_bands = deepcopy(tax_bands)	
	while earned != 0:
		if tmp_bands and earned < tmp_bands[0][0]:
			tmp_bands[0][0] -= earned
			earned = 0
		elif tmp_bands:
			earned -= tmp_bands[0][0]
			tmp_bands = tmp_bands[1:]
		else:
			earned = 0
	j = 0
	while j < len(tmp_bands) and to_give != 0:
		band = tmp_bands[j]
		if band[1] != 100:
			if band[1] == 0:
				can_get = band[0]
			else:
				can_get = band[0]/100*(100-band[1])
			if can_get >= to_give and band[1] == 0:
				total += to_give
				to_give = 0
			elif can_get >= to_give:
				total += to_give/(100-band[1])*100
				to_give = 0
			else:
				total += band[0]
				to_give -= can_get
		else:
			total += band[0]
		j += 1
	if to_give != 0:
		if final_tax == 0:
			total += to_give
		else:
			total += to_give/(100-final_tax)*100
	print("{:.6f}".format(total))
