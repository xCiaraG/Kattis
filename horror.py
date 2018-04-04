from sys import stdin
N, H, L = [int(x) for x in stdin.readline().split()]
horrors = [int(x) for x in stdin.readline().split()]
HI = {}
edges = {}

for i in range(N):
   edges[i] = []

for horror in horrors:
   HI[horror] = 0

for _ in range(L):
   u, v = [int(x) for x in stdin.readline().split()]
   edges[u].append(v)
   edges[v].append(u)

while horrors:
   to_check = horrors
   horrors = []
   for i in to_check:
      for j in edges[i]:
         if j not in HI:
             HI[j] = HI[i] + 1
             horrors.append(j)
max_found = 0
max_index = 0
for i in range(N):
   if i not in HI and float('inf') > max_found:
      max_found = float('inf')
      max_index = i
   elif i in HI and HI[i] > max_found:
      max_found = HI[i]
      max_index = i
print(max_index)