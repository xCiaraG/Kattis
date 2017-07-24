import sys
line = sys.stdin.readline().strip()
def always_up(s):
    count = 0
    previous = s[0]
    for c in s[1:]:
        if previous == "D":
            count += 1
        elif c == "D":
            count += 2
        previous = "U"
    return count

def always_down(s):
    count = 0
    previous = s[0]
    for c in s[1:]:
        if previous == "U":
            count += 1
        elif c == "U":
            count += 2
        previous = "D"
    return count

def like_to_find(s):
    count = 0
    previous = s[0]
    for c in s[1:]:
        if previous != c:
            count += 1
        previous = c
    return count

print(always_up(line))
print(always_down(line))
print(like_to_find(line))
