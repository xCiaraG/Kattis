import sys
line = sys.stdin.readline().strip()
d = {}
while line != "***":
    if line not in d:
        d[line] = 1
    else:
        d[line] += 1
    line = sys.stdin.readline().strip()

m = 0
m_person = []
for key in d:
    if d[key] > m:
        m = d[key]
        m_person = [key]
    elif d[key] == m:
        m_person.append(key)
if len(m_person) == 1:
    print(m_person[0])
else:
    print("Runoff!")
