import itertools
se = []
for i in range(0, 4):
    line = list(input().strip().split())
    se += line
i = 0
while i < len(se):
    se[i] += str(i+1)
    i += 1
tmp = list(itertools.combinations(se, 3))
ans = []
for s in tmp:
    tmp1 = set([s[0][0], s[1][0], s[2][0]])
    tmp2 = set([s[0][1], s[1][1], s[2][1]])
    tmp3 = set([s[0][2], s[1][2], s[2][2]])
    tmp4 = set([s[0][3], s[1][3], s[2][3]])
    if (len(tmp1) == 1 or len(tmp1) == 3) and (len(tmp2) == 1 or len(tmp2) == 3) and (len(tmp3) == 1 or len(tmp3) == 3) and (len(tmp4) == 1 or len(tmp4) == 3):
        ans.append(sorted([int(s[0][4:]), int(s[1][4:]), int(s[2][4:])]))
ans = sorted(ans)
if ans:
    for a in ans:
        print(*a)
else:
    print("no sets")
