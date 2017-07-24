from operator import itemgetter
line = input().strip().split()
n = int(input())
d = {}
m = {}
order = []
for i in range(0, n):
   tmp = input().strip().split()
   d[i] = tmp
   tmp_map = {}
   j = 0
   while j < len(line):
      tmp_map[line[j]] = tmp[j]
      j += 1
   m[i] = tmp_map
   order.append(i)
n = int(input())
for i in range(0, n):
   sort_by = input().strip()
   to_print = []
   for j in order:
      to_print.append((m[j][sort_by], j))
   to_print = sorted(to_print, key=itemgetter(0))
   order = [t[1] for t in to_print]
   print(" ".join(line))
   for t in to_print:
      print(" ".join(d[t[1]]))
   if i != n-1:
      print()