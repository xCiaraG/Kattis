import sys
left = []
right = []
for i in range(0,3):
    n = list(map(int, sys.stdin.readline().strip().split()))
    left.append(n[0])
    right.append(n[1])
if left[0] == left[1]:
    tmp = left[2]
elif left[1] == left[2]:
    tmp = left[0]
else:
    tmp = left[1]

if right[0] == right[1]:
    tmp2 = right[2]
elif right[1] == right[2]:
    tmp2 = right[0]
else:
    tmp2 = right[1]
print(tmp, tmp2)
