from sys import stdin
n = input()
for i in range(n):
	s = raw_input()
	t = raw_input()
	d = {"0" : 0, "1" : 0, "?" : 0}
	if len(s) != len(t) or s.count("1") > t.count("1"):
		print("Case {}: -1".format(i + 1))
	else:
		for j in range(len(s)):
			if s[j] != t[j]:
				d[s[j]] += 1
		if  d["0"] >= d["1"]:
			d["0"] -= d["1"]
		else:
			d["1"] -= d["0"]
		ans = d["0"] + d["1"] + d["?"]
		print("Case {}: {}".format(i + 1, ans))
