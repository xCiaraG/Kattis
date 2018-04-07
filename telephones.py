from sys import stdin
n, m = [int(x) for x in stdin.readline().split()]
while n + m != 0:
  intervals = []
  for i in range(n):
    s, d, start, duration = [int(x) for x in stdin.readline().split()]
    if duration > 0:
      intervals.append((start, start + duration))
  for i in range(m):
    count = 0
    start, duration = [int(x) for x in stdin.readline().split()]
    if duration > 0:
      for x, y in intervals:
        if (start + duration < y and start + duration > x) or (start >= x and start < y) or (start < x and start + duration >= y):
          count += 1
    print(count)
  n, m = [int(x) for x in stdin.readline().split()]