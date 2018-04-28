from sys import stdin
n, m = [int(x) for x in stdin.readline().split()]
parts = set()
finished = False
for i in range(m):
   parts.add(stdin.readline().strip()) 
   if not finished and len(parts) == n:
      finished = True
      print(i + 1)
if len(parts) < n:
   print('paradox avoided')