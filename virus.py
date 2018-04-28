s1 = raw_input().strip()
s2 = raw_input().strip()
i = 0
while i < len(s1) and i < len(s2) and s1[i] == s2[i]:
    i += 1

j = -1
while -j < len(s1) and -j < len(s2) and s1[j] == s2[j] and (len(s2) + j) >= i and (len(s1) + j) >= i:
    j -= 1
print(len(s2) + j - i + 1)