import sys
notes = {"A#":"Bb", "Bb":"A#", "C#": "Db", "Db":"C#", "D#": "Eb", "Eb":"D#", "F#": "Gb", "Gb": "F#",
		"G#":"Ab", "Ab": "G#"}
lines = sys.stdin.readlines()
i = 1
for line in lines:
	line = line.split()
	if line[0] in notes:
		print("Case {}: {} {}".format(i, notes[line[0]],line[1]))
	else:
		print("Case {}: UNIQUE".format(i))
	i += 1