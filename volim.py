import sys
person = int(sys.stdin.readline().strip())
n = int(sys.stdin.readline().strip())
count = 0
a = True
for i in range(0, n):
    line = sys.stdin.readline().strip().split()
    count += int(line[0])
    if count >= 210 and a:
        exploding_person = person % 8
        a = False
    if line[1] == "T":
        person += 1
if exploding_person == 0:
    exploding_person = 8
print(exploding_person)
