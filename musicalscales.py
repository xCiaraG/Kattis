notes = ["A", "A#", "B", "C", "C#", "D", "D#", "E", "F", "F#", "G", "G#"]
scale = [2, 4, 5, 7, 9, 11, 12]
valid_scales = {}
for i in range(12):
	current = set()
	for t in scale:
		current.add(notes[(i+t) % 12])
	valid_scales[notes[i]] = current
ans = []
n = int(input())
song = set(input().split())
for n in notes:
	if len(valid_scales[n].intersection(song)) == len(song):
		ans.append(n)
if ans:
	print(*ans)
else:
	print("none")
