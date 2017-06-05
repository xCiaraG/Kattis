def triangle_area(x1, y1, x2, y2, x3, y3):
	tmp = abs(x1*(y2-y3)+x2*(y3-y1)+x3*(y1-y2))
	return tmp/2

line1 = list(map(int, input().strip().split()))
line2 = list(map(int, input().strip().split()))
line3 = list(map(int, input().strip().split()))
x1, y1, x2, y2, x3, y3 = line1[0], line1[1], line2[0], line2[1], line3[0], line3[1]
area = triangle_area(x1, y1, x2, y2, x3, y3)
n = int(input())
count = 0
for i in range(0, n):
	line = list(map(int, input().strip().split()))
	x4, y4 = line[0], line[1]
	if area == triangle_area(x1, y1, x4, y4, x3, y3) + triangle_area(x1, y1, x2, y2, x4, y4) + triangle_area(x4, y4, x2, y2, x3, y3):
		count += 1
print(area)
print(count)

