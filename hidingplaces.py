from sys import stdin

abc = 'abcdefgh'
n = int(stdin.readline())
for i in range(n):
   moves = {}
   place = stdin.readline().strip()
   to_check = [(abc.index(place[0]) + 1, int(place[1]), 0)]
   while to_check:
      i, j, count = to_check.pop(0)
      if (i, j) not in moves and 1 <= i <= 8 and 1 <= j <= 8:
         moves[(i, j)] = count
      to_check.append((i + 2, j + 1, count + 1))
      to_check.append((i + 1, j + 2, count + 1))
      to_check.append((i - 2, j + 1, count + 1))
      to_check.append((i + 2, j - 1, count + 1))
      to_check.append((i - 1, j + 2, count + 1))
      to_check.append((i + 1, j - 2, count + 1))
      to_check.append((i - 2, j - 1, count + 1))
      to_check.append((i - 1, j - 2, count + 1))
   max_vals = []
   max_val = 0
   for k in moves:
      if moves[k] > max_val:
         max_val = moves[k]
     max_vals = [k]
      elif moves[k] == max_val:
         max_vals.append(k)
   max_vals = [abc[a - 1] + str(b) for a, b in max_vals]
   max_vals = sorted(max_vals, key = lambda x: (-int(x[1]), x[0]))
   print max_val, " ".join(max_vals)