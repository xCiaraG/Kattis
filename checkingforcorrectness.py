from sys import stdin   
def add(n1, n2):
    return n1 + n2

def multiply(n1, n2):
    return  n1 * n2

lines = stdin.readlines()
for line in lines:
    line = line.strip().split()
    if line[1] == "+":
        n = add(int(line[0][-4:]), int(line[2][-4:]))
    elif line[1] == "*":
        n = multiply(int(line[0][-4:]), int(line[2][-4:]))
    else:
        n = pow(int(line[0]), int(line[2]), 10000)
    n = str(n)
    n = int(n[-4:])
    print(n)
