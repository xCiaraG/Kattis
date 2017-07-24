mport sys
line = sys.stdin.readline().strip()
new_line = ""
for c in line:
    if len(new_line) == 0 or new_line[len(new_line)-1] != c:
        new_line += c
print(new_line)
