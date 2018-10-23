from sys import stdin
def main():
	n = int(stdin.readline())
	for _ in range(n):
		digits = [int(x) for x in list(stdin.readline().strip())]
		for i in range(len(digits)-2, -1, -2):
			d = str(2*digits[i])
			if len(d) == 2:
				digits[i] = int(d[0]) + int(d[1])
			else:
				digits[i] = int(d)
		if sum(digits) % 10 == 0:
			print('PASS')
		else:
			print('FAIL')

if __name__ == '__main__':
	main()