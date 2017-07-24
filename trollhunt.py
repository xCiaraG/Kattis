line = list(map(int, input().strip().split()))
groups = line[1]//line[2]
if (line[0]-1) % groups == 0:
    print((line[0]-1)//groups)
else: 
    print(((line[0]-1)//groups)+1)
