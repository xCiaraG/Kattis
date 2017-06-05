import sys
d = "\][POIUYTREWQ';LKJHGFDSA/.,MNBVCXZ=-0987654321`"
lines = sys.stdin.readlines()
for line in lines:
	line = line.strip()
	new_s = ""
	for c in line:
	    if c == " ":
	        new_s += " "
	    else:
	        new_s += d[d.index(c)+1]

	print(new_s)