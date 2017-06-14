import random, string
line = list(map(int, input().strip().split()))
s = [0]*line[1]
for i in range(0, line[1]):
	s[i] = ("".join([random.choice(string.ascii_lowercase) for n in range(15)]))

print(" ".join(s))
	