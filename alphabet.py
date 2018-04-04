def lcs(s1, s2):
    table = [[0 for i in range(len(s1) + 1)] for j in range(len(s2) + 1)]
    for i in range(1, len(s2)+1):
        for j in range(1, len(s1)+1):
            if s2[i-1] == s1[j-1]:
                table[i][j] = 1 + table[i-1][j-1]
            else:
                table[i][j] = max(table[i-1][j], table[i][j-1])
    return table[-1][-1]

alphabet = "abcdefghijklmnopqrstuvwxyz"
s = input().strip()
print(26 - lcs(s, alphabet))