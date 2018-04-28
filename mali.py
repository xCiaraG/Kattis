from sys import stdin

def find_max(l1, l2):
   max_found = 0
   i_start, j_start = 1, 1
   i_end, j_end = 100, 100
   while l1[i_start] == 0:
      i_start += 1
   while l1[i_end] == 0:
      i_end -= 1
   while l2[j_start] == 0:
      j_start += 1
   while l2[j_end] == 0:
      j_end -= 1

   while i_start <= i_end:
      if i_start + j_end > max_found:
         max_found = max(max_found, i_end + j_start)
         if l1[i_end] < l2[j_start]:
            l2[j_start] -= l1[i_end]
            i_end -= 1
         else:
            l1[i_end] -= l2[j_start]
            j_start += 1
      elif l1[i_start] < l2[j_end]:
         l2[j_end] -= l1[i_start]
         i_start += 1
      else:
         l1[i_start] -= l2[j_end]
         j_end -= 1

      while l1[i_start] == 0:
         i_start += 1
      while l1[i_end] == 0:
         i_end -= 1
      while l2[j_start] == 0:
         j_start += 1
      while l2[j_end] == 0:
         j_end -= 1
   
   return max_found

n = int(stdin.readline())
a1, b1 = [1] + [0]*100 + [1], [1] + [0]*100 + [1]
a2, b2 = [1] + [0]*100 + [1], [1] + [0]*100 + [1]
for i in range(n):
   a, b = [int(x) for x in stdin.readline().split()]
   a1[a] += 1
   b1[b] += 1
   for i in range(101):
      a2[i] = a1[i]
      b2[i] = b1[i]
   print(find_max(a2, b2))