n = int(input())
t = 0
probabilities = []
for i in range(0, n):
    line = input().strip().split()
    probabilities.append(float(line[1]))
probabilities = sorted(probabilities)
probabilities.reverse()
for i in range(0, n):
    t += (i+1) * probabilities[i]

print(t)
