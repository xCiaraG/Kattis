from sys import stdin
def merge(a, b):
   l = []
   while a and b:
      l.append(a.pop(0))
      l.append(b.pop(0))
   while a:
      l.append(a.pop(0))
   return l

def in_out(cmd, n):
   l = [i for i in range(1, n + 1)]
   tmp = True
   count = 0
   if n % 2 == 0 or cmd == "in" and n % 2 == 1:
      i = n // 2
   else:
      i = n // 2 + 1

   while tmp or sorted(l) != l:
      tmp = False
      a = l[:i]
      b = l[i:]
      if cmd == "out":
         l = merge(a, b)
      else: 
         l = merge(b, a)
      count += 1
   return count

n, cmd = stdin.readline().strip().split()
print(in_out(cmd, int(n)))