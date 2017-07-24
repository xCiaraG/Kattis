import sys, math
n = list(map(float,sys.stdin.readline().strip().split()))
a = ((math.pi*(n[0]**2)-( math.pi*((n[1]-n[0])**2) ))/(math.pi*(n[0]**2)) * 100)
print("{:.6f}".format(100 - a))
