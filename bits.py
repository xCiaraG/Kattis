n = int(input())
for i in range(0, n):
	num = input().strip()
	m = 0
	j = 1
	while j < len(num)+1:
		tmp = int(num[:j])
		tmp = str(bin(tmp)[2:])
		if tmp.count("1") > m:
			m = tmp.count("1")
		j += 1
	print(m)
	
