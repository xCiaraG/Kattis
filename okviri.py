import sys
line = sys.stdin.readline().strip()
peter_top_bottom = "..#."
peter_second = ".#.#"
wendy_top_bottom = "..*."
wendy_second = ".*.*"
s1 = ""
s2 = ""
s3 = ""
s4 = ""
s5 = ""
a = False
count = 1
for letter in line:
    if count % 3 != 0:
        s1 += peter_top_bottom
        s2 += peter_second
        if a and (count - 1) % 3 == 0:
            s3 += "*." + letter + "."
        else:
            s3 += "#." + letter + "."
        s4 += peter_second
        s5 += peter_top_bottom
    else:
        s1 += wendy_top_bottom
        s2 += wendy_second
        s3 += "*." + letter + "."
        s4 += wendy_second
        s5 += wendy_top_bottom
    count += 1
    a = True
print(s1 + ".")
print(s2 + ".")
if (count - 1) % 3 != 0:
    print(s3 + "#")
else:
    print(s3 + "*")
print(s4 + ".")
print(s5 + ".")
