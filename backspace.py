line = input().strip()
length = len(line)
tmp = []
c = 0
i = 0
while i < length:
   t = line[i]
   if t == "<" and c:
      tmp.pop()
      c -= 1
   elif t != "<":
      tmp.append(line[i]) 
      c += 1
   i += 1
if tmp:
   print("".join(tmp))