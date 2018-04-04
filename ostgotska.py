sentence = input().strip().split()
total = 0
for word in sentence:
	if "ae" in word:
		total += 1

if total / len(sentence) >= .4:
	print("dae ae ju traeligt va")
else:
	print("haer talar vi rikssvenska")