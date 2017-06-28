n = int(input().strip())
platforms = []
for i in range(0, n):
   platforms.append(list(map(int, input().strip().split())))
platforms = sorted(platforms, reverse=True)
count = 0
j = 0
while j < len(platforms):
   p = platforms[j]
   k = j + 1
   lhs = p[1]
   rhs = p[2]
   a, b = True, True
   while (a or b) and (k < len(platforms)):
      tmp = platforms[k]
      if a and tmp[1] +.5  <= lhs +.5 <= -.5 + tmp[2]:
         count += p[0] - tmp[0]
         a = False
      if b and tmp[1] +.5 <= rhs-.5 <= -.5 + tmp[2]:
         count += p[0] - tmp[0]
         b = False
      k += 1
   if a:
      count += p[0]
   if b:
      count += p[0]
   j += 1
print(count)