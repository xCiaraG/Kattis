import math
n = map(int, raw_input().strip().split())
def one(n, m):
    a, i = 1, 1
    while n > a and i < m+1:
        a *= i
        i += 1
    return n >= a
def two(n, m):
    t, a = 2, 2
    i = 1
    while n > a and i < m:
        a *= t
        i += 1
    return n >= a
def three(n, m):
    return n >= m**4
def four(n, m):
    return n >= m**3
def five(n, m):
    return n >= m**2
def six(n, m):
    return n >= m*(math.log(m)/math.log(2))
def seven(n, m):
    return n >= m

if n[2] == 1:
    a = one(n[0], n[1])
elif n[2] == 2:
    a = two(n[0], n[1])
elif n[2] == 3:
    a = three(n[0], n[1])
elif n[2] == 4:
    a = four(n[0], n[1])
elif n[2] == 5:
    a = five(n[0], n[1])
elif n[2] == 6:
    a = six(n[0], n[1])
else:
    a = seven(n[0], n[1])

if a:
    print("AC")
else:
    print("TLE")