to_find = input().strip()
start, end = True, True
if to_find[0] != "*":
	start = False
if to_find[-1] != "*":
	end = False
to_find = to_find.split("*")
n = int(input())
for i in range(0, n):
	word = input().strip()
	tmp_start, tmp_end, i, j, k, l = start, end, 0, len(word), 0, len(to_find)
	if not start and word.startswith(to_find[0]):
		i += len(to_find[0])
		k += 1
		tmp_start = True
	if not end and k < l and word[i:j].endswith(to_find[-1]):
		j -= len(to_find[-1])
		l -= 1
		tmp_end = True
	a = True
	while k < l and a:
		if to_find[k] in word[i:j]:
			i += word[i:j].index(to_find[k]) + len(to_find[k])
			k += 1
		else:
			a = False
	if a and tmp_start and tmp_end:
		print(word)

	

