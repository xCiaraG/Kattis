import sys
lines = sys.stdin.readlines()
for line in lines:
    line = line.rstrip()
    one = 0 
    zero = 0
    for letter in line:
        tmp = bin(ord(letter))[2:]
        if len(tmp) < 7:
            tmp += "0"*(7-len(tmp))
        one += tmp.count("1")
        zero += tmp.count("0")
    if one % 2 == 0 and zero % 2 == 0:
        print("free")
    else:
        print("trapped")