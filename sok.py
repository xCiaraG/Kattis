ratios = list(map(int, input().strip().split()))
juices = list(map(int, input().strip().split()))
smallest = ratios[0]/juices[0]
smalln = 0
to_d = ratios[0]/juices[0]
if smallest > ratios[1]/juices[1]:
    smallest = ratios[1]/juices[1]
    smalln = 1
    to_d = ratios[1]/juices[1]
if smallest > ratios[2]/juices[2]:
    smalln = 2
    to_d = ratios[2]/juices[2]

out = []
for i in range(0, 3):
    if smalln == i:
        out.append(0)
    else:
        n = ratios[i] - juices[i]*to_d
        n = n / juices[i]
        out.append(n)

print("{:.6f} {:.6f} {:.6f}".format(out[0]*juices[0], out[1]*juices[1], out[2]*juices[2]))
