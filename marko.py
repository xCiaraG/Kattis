import sys
n = int(sys.stdin.readline().strip())
d = {"a":"2","b": "2","c":"2","d":"3","e":"3","f":"3",
     "g":"4","h":"4","i":"4","j":"5","k":"5","l":"5",
     "m":"6","n":"6","o":"6","p":"7","q":"7","r":"7",
     "s":"7","t":"8","u":"8","v":"8","w":"9","x":"9",
     "y":"9","z":"9"}
word_string = []
for i in range(0,n):
    word = sys.stdin.readline().strip()
    s = ""
    for letter in word:
        s += d[letter]
    word_string.append(s)

numbers = input()
print(word_string.count(numbers))
