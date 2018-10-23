a, b = input().split()
for l in a:
  if l in b:
    a_pos = a.find(l)
    b_pos = b.find(l)
    break
for i in range(len(b)):
  current = ["."] * len(a)
  current[a_pos] = b[i]
  if i == b_pos:
    current = list(a)
  print("".join(current))