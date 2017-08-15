from sys import stdin
def num_flies(i, j):
	s = 0
	for k in range(i+1, i+racket-1):
		s += window[k][j+1:j+racket-1].count("*")
	return s

def draw_racket(mx, my):
	window[mx][my] = "+"
	window[mx][my+racket-1] = "+"
	window[mx+racket-1][my] = "+"
	window[mx+racket-1][my+racket-1] = "+"
	for i in range(my+1, my+racket-1):
		window[mx][i] = "-"
		window[mx+racket-1][i] = "-"
	for i in range(mx+1, mx+racket-1):
		window[i][my] ="|"
		window[i][my+racket-1] = "|"

x, y, racket = [int(x) for x in stdin.readline().split()]
window = [0]*x
for i in range(0, x):
	window[i] = list(stdin.readline().strip())

m, mx, my = 0, 0, 0
i = 0
while i <= x - racket:
	j = 0
	while j <= y - racket:
		tmp = num_flies(i, j)
		if tmp > m:
			m, mx, my = tmp, i, j
		j += 1
	i += 1

print(m)
draw_racket(mx, my)
for line in window:
	print("".join(list(map(str, line))))