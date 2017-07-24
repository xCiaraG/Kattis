line = list(map(int, input().strip().split()))
seating = []
for i in range(0, line[0]):
    seating.append(input().strip())
m = 0
j = 0
while j < len(seating):
    k = 0
    while k < len(seating[j]):
        count = 0
        if seating[j][k] == ".":
            if k > 0 and seating[j][k-1] == "o":
                count += 1
            if k + 1 < len(seating[j]) and seating[j][k+1] == "o":
                count += 1
            if j > 0 and seating[j-1][k] == "o":
                count += 1
            if j + 1 < len(seating) and seating[j+1][k] == "o":
                count += 1
            if k > 0 and j > 0 and seating[j-1][k-1] == "o":
                count += 1
            if j + 1 < len(seating) and k + 1 < len(seating[j]) and seating[j+1][k+1] == "o":
                count += 1
            if k > 0 and j + 1 < len(seating) and seating[j+1][k-1] == "o":
                count += 1
            if j > 0 and k + 1 < len(seating[j]) and seating[j-1][k+1] == "o":
                count += 1
            if count > m:
                m = count
                x, y = j, k
        k += 1
    j += 1
if m:
    seating[x] = seating[x][:y] + "o" + seating[x][y+1:]

i = 0
count = 0
while i < len(seating):
    j = 0
    while j < len(seating[i]):
        if seating[i][j] == "o":
            if j + 1 < len(seating[i]) and seating[i][j+1] == "o":
                count += 1
            if i + 1 < len(seating) and seating[i+1][j] == "o":
                count += 1
            if i + 1 < len(seating) and j > 0 and seating[i+1][j-1] == "o":
                count += 1
            if i + 1 < len(seating) and j + 1 < len(seating[i]) and seating[i+1][j+1] == "o":
                count += 1 
        j += 1
    i += 1
print(count)
