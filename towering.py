line = list(map(int, input().strip().split()))
h1 = line[6]
h2 = line[7]
line = line[:-2]
i = 0
while i < len(line):
    j = 0
    while j < len(line):
        k = 0
        while k < len(line):
            if i != j and j != k and i != k and line[i] + line[j] + line[k] == h1:
                h1_boxes = [line[i], line[j], line[k]]
                line.remove(h1_boxes[0])
                line.remove(h1_boxes[1])
                line.remove(h1_boxes[2])
            k += 1
        j += 1
    i += 1
h1_boxes = sorted(h1_boxes)
h1_boxes.reverse()
line = sorted(line)
line.reverse()
answer = h1_boxes + line
answer = list(map(str, answer))
print(" ".join(answer))
