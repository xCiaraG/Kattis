word = input().strip()
earliest = word
for i in range(1, len(word)):
	for j in range(i + 1, len(word)):
		tmp = word[:i][::-1] + word[i:j][::-1] + word[j:][::-1]
		if tmp < earliest:
			earliest = tmp
print(earliest)