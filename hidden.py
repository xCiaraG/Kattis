import sys
line = sys.stdin.readline().strip().split()
password = line[0]
word = line[1]
i = 0
a = True
while password and i < len(word):
    if word[i] == password[0]:
        if len(password) > 1:
            password = password[1:]
        else:
            password = ""
    elif word[i] in password:
        a = False
    i += 1
if not password and a:
    print("PASS")
else:
    print("FAIL")
