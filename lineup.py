import sys
n = int(sys.stdin.readline().strip())
names = []
for i in range(0, n):
    name = sys.stdin.readline().strip()
    names.append(name)

new_names = names[:]
new_names.sort()
new_names2 = new_names[:]
new_names2.reverse()
if new_names == names:
    print("INCREASING")
elif new_names2 == names:
    print("DECREASING")
else:
    print("NEITHER")
