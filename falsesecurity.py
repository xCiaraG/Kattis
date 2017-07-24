import sys
d_to_morse = {"A":".-","H":"....","O":"---","V":"...-","B":"-...","I":"..","P":".--.","W":".--","C":"-.-.","J":".---","Q":"--.-","X":"-..-",
    "D":"-..","K":"-.-","R":".-.","Y":"-.--","E":".","L":".-..","S":"...","Z":"--..","F":"..-.","M":"--","T":"-","G":"--.","N":"-.",
    "U":"..-","_":"..--",".":"---.",",":".-.-","?":"----"}
d_from_morse = {}
for key in d_to_morse:
    d_from_morse[d_to_morse[key]] = key
def convert_to_morse(s):
    new_string = ""
    numbers = ""
    for letter in s:
        new_string += d_to_morse[letter]
        numbers += str(len(d_to_morse[letter]))
    return [new_string, numbers]

def convert_to_string(s, numbers):
    i= 0 
    new_string = ""
    current = 0
    while i < len(numbers):
        new_string += d_from_morse[s[current:current + int(numbers[i])]]
        current += int(numbers[i])
        i += 1
    return new_string

lines = sys.stdin.readlines()
for line in lines:
    line = line.strip()
    li = convert_to_morse(line)
    new_s = convert_to_string(li[0], li[1][::-1])
    print(new_s)
