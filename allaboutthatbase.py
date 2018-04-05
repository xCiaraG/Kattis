def to_decimal(number, system):
    b = len(system)
    number = number[::-1]
    total = 0
    i = 0
    while i < len(number):
        total += (b**i)*(system.index(number[i]))
        i += 1
    return total

def summ(a, b):
    return a + b

def sub(a, b):
    return a - b

def div(a, b):
    return a / b

def mul(a, b):
    return a * b

bases = "0123456789abcdefghijklmnopqrstuvwxyz0"
d = {"+" : summ, "-" : sub, "/" : div, "*" : mul}
n = int(input())
for i in range(0, n):
    start = 1
    ans = ""
    line = input().strip().split()
    start = bases.index(max(line[0] + line[2] + line[4]))
    if start == 1 and set(line[0] + line[2]) == set("1") and (line[4] == "0" or set(line[4]) == set("1")):
        tmp = d[line[1]](len(line[0]), len(line[2]))
        if line[4] == "0":
            tmp_ans = 0
        else:
            tmp_ans = len(line[4])
        if tmp == tmp_ans:
            ans += "1"
    for j in range(start, len(bases) - 1):
        if to_decimal(line[0], bases[:j+1]) <= (2**32) - 1 and to_decimal(line[2], bases[:j+1]) <= (2**32) - 1 and to_decimal(line[4], bases[:j+1]) <= (2**32) - 1:
            if d[line[1]](to_decimal(line[0], bases[:j+1]), to_decimal(line[2], bases[:j+1])) == to_decimal(line[4], bases[:j+1]):
                ans += bases[j+1]
    if ans:
        print(ans)
    else:
        print("invalid")