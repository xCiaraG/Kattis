import sys
n = int(sys.stdin.readline().strip())
line = sys.stdin.readline().strip()
Adrian_s = "ABC"
Bruno_s = "BABC"
Goran_s = "CCAABB"
d = {"Bruno":0, "Adrian":0, "Goran":0}
for i in range(0,len(line)):
    if line[i] == Bruno_s[i % len(Bruno_s)]:
        d["Bruno"] += 1
    if line[i] == Adrian_s[i % len(Adrian_s)]:
        d["Adrian"] += 1
    if line[i] == Goran_s[i % len(Goran_s)]:
        d["Goran"] += 1

best_student = []
best_score = -1
for key in d:
    if d[key] > best_score:
        best_score = d[key]
        best_student = [key]
    elif d[key] == best_score:
        best_student.append(key)

print(best_score)
for student in sorted(best_student):
    print(student)
