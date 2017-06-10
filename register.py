line = list(map(int, input().strip().split()))
v2 = line[0]
v3 = line[1]
v5 = line[2]
v7 = line[3]
v11 = line[4]
v13 = line[5]
v17 = line[6]
v19 = line[7]
t = (18 - v19) * 510510
t += (16 - v17) * 30030
t += (12 - v13) * 2310
t += (10 - v11) * 210
t += (6 - v7) * 30
t += (4 - v5) * 6
t += (2 - v3) * 2
t += (1 - v2)
print(t)