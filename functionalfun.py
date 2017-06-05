import sys
def injective(codomain):
	tmp = []
	for k in d:
		tmp.append(d[k])
	if len(set(tmp)) == len(tmp):
		return True
	return False

def surjective(codomain):
	tmp = codomain[:]
	for k in d:
		if d[k] in tmp:
			tmp.remove(d[k])
	if not tmp:
		return True
	return False

lines = sys.stdin.readlines()
i = 0
while i < len(lines):
	domain = lines[i].strip().split()[1:]
	codomain = lines[i+1].strip().split()[1:]
	n = int(lines[i+2].strip())
	d = {}
	a = True
	i += 3
	for j in range(0, n):
		tmp = lines[i].strip().split()
		if tmp[0] not in d:
			d[tmp[0]] = tmp[-1]
		else:
			a = False
		i += 1
	if a and surjective(codomain) and injective(codomain):
		print("bijective")
	elif a and injective(codomain):
		print("injective")
	elif a and surjective(codomain):
		print("surjective")
	elif a: 
		print("neither injective nor surjective")
	else:
		print("not a function")


