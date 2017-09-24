price, zeros = [int(x) for x in input().split()]
d = int("1"+("0"*zeros))
if price % d == 0:
	print(price)
elif price == 0:
	print(0)
else:
	tmp = "{:.{}f}".format(price/d, zeros).split(".")
	n = float("." + tmp[1])
	if n < .5:
		print(int(tmp[0]+"0"*zeros))
	else:
		print(int(str(int(tmp[0])+1)+"0"*zeros))
