import sys
def convert_word(s):
    vowels = "aeiouy"
    if s[0] in vowels:
        return s + "yay"
    i = 0
    while s[i] not in vowels:
        i += 1
    return s[i:] + s[:i] + "ay"

lines = sys.stdin.readlines()
for line in lines:
    line = line.strip().split()
    sentance = ""
    for word in line:
        sentance += convert_word(word) + " "
    print(sentance.strip())
