import sys
def A(l):
    tmp = l[0]
    l[0] = l[1]
    l[1] = tmp
    return l

def B(l):
    tmp = l[2]
    l[2] = l[1]
    l[1] = tmp
    return l

def C(l):
    tmp = l[0]
    l[0] = l[2]
    l[2] = tmp
    return l

line = sys.stdin.readline().strip()
l = [1, 0, 0]
for c in line:
    if c == "A":
        l = A(l)
    elif c == "B":
        l = B(l)
    elif c == "C":
        l = C(l)
i = 0
while i < len(l):
    if l[i] == 1:
        print(i + 1)
    i += 1
