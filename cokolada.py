n = int(input().strip())
i = 0

while 2**i < n:
   i += 1

barsize = 2**i
breaks = 0
tmpbar = barsize
while n != 0:
   if n - tmpbar < 0:
      breaks += 1
      tmpbar = tmpbar // 2
   else:
      n -= tmpbar

print(barsize, breaks)