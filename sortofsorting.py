n = int(input())
while n != 0:
	words = []
	to_sort = []
	to_sort2 = []
	for i in range(0, n):
		word = input().strip()
		if len(word) > 1:
			words.append(word)
			to_sort.append(word[:2])
			to_sort2.append(word[:2])
		else:
			words.append(word)
			to_sort.append(word)
			to_sort2.append(word2)
	to_sort2 = sorted(to_sort2)
	i = 0 
	while i < len(to_sort2):
		tmp = to_sort2[i]
		ind = to_sort.index(tmp)
		to_sort.remove(tmp)
		to_sort2[i] = words[ind]
		words.remove(words[ind])
		i += 1
	for word in to_sort2:
		print(word)

	n = int(input())
	if n != 0:
		print()	
