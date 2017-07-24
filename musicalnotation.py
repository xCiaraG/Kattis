import sys
n = sys.stdin.readline()
d1 = {"a": "a: ", "e": "e: ", "g": "g: ", "B": "B: ", "D": "D: ", "F": "F: "} 
d2 = {"b": "b: ", "c": "c: ", "d": "d: ", "e": "e: ", "f": "f: ", "A": "A: ",
      "C": "C: ", "E": "E: ", "G": "G: "}
line = sys.stdin.readline().strip().split()
for note in line:
    if len(note) == 1:
        x = 1
    else:
        x = int(note[1:])
    note = note[0]
    for n in d1:
        if n == note:
            d1[n] += "*"*x + "-"
        else:
            d1[n] += "-"*x + "-"
    for n in d2:
        if n == note:
            d2[n] += "*"*x + " "
        else:
            d2[n] += " "*x + " "

for letter in "GFEDCBAgfedcba":
    if letter in d1:
        print(d1[letter][:len(d1[letter])-1])
    else:
        print(d2[letter][:len(d2[letter])-1])
