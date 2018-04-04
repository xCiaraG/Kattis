from sys import stdin
n = int(stdin.readline().strip())
categories = {}
d = {}
for i in range(n):
   category = [x for x in stdin.readline().strip().split()]
   categories[category[0]] = category[2:]
   for word in category[2:]:
      d[word] = 0
lines = stdin.readlines()
for line in lines:
   line = line.strip().split()
   for word in line:
      if word in d:
         d[word] += 1
sums = [(category, sum([d[i] for i in categories[category]])) for category in categories]
ans = max(sums, key=lambda x: x[1])[1]
for word in sorted([x[0] for x in sums if x[1] == ans]):
   print(word)