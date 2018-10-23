from sys import stdin

def main():
	rain = stdin.readline().strip()
	blue, red, largest = 0, 0, 0
	red_left, blue_left, i = 1, 1, 0
	d = {'R' : [1, -1], 'B' : [-1, 1]}
	for colour in rain:
		i += 1
		red += d[colour][0]
		blue += d[colour][1]
		if blue < 0:
			blue_left = i + 1
			blue = 0
		if red < 0:
			red_left = i + 1
			red = 0
		if red > largest:
			largest = red
			max_left = red_left
			max_right = i
		if blue > largest:
			largest = blue
			max_left = blue_left
			max_right = i

	print max_left, max_right

if __name__ == '__main__':
	main()