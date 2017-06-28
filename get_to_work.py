n = int(input().strip())
for i in range(0, n):
   line = list(map(int, input().strip().split()))
   towns = line[0]
   work = line[1]
   d = {}
   for j in range(1, line[0] + 1):
      d[j] = []
   m = int(input().strip())
   for j in range(0, m):
      line = list(map(int, input().strip().split()))
      d[line[0]].append(line[1])
   ans = [0]*towns
   a = True
   for n in d:
      if n != work:
         tmp = d[n]
         tmp = sorted(tmp, reverse=True)
         t = 0
         while tmp and a and n != work:
            if tmp[0] == 0:
               a = False
            else:
               t += 1
               num = tmp[0] - 1
               tmp.remove(tmp[0])
               if len(tmp) - num < 0:
                  tmp = []
               else:
                  tmp = tmp[:len(tmp)-num]
         ans[n-1] = t
   if a:
      ans = list(map(str, ans))
      print("Case #{}: {}".format(i+1, " ".join(ans)))
   else:
      print("Case #{}: IMPOSSIBLE".format(i+1))