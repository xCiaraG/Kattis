import sys
line = sys.stdin.readline().strip()
whitespace = 0
lower = 0
upper = 0
other = 0
s_lower = "abcdefghijklmnopqrstuvwxyz"
s_upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
for c in line:
    if c in s_lower:
        lower += 1
    elif c in s_upper:
        upper += 1
    elif c == "_":
        whitespace += 1
    else:
        other += 1

print("{:.16f}".format(whitespace/len(line)))
print("{:.16f}".format(lower/len(line)))
print("{:.16f}".format(upper/len(line)))
print("{:.16f}".format(other/len(line)))
