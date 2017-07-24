import math 
line = input().strip().split()
number = math.sqrt(int(line[1])**2 + int(line[2])**2)
for i in range(0, int(line[0])):
    num = int(input().strip())
    if num <= number:
        print("DA")
    else:
        print("NE")
