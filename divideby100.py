n = input().strip()
m = input().strip()
n_length = len(n)
m_length = len(m) - 1
if n_length == m_length:
	ans = "0." + n
	a = True
elif m_length < n_length:
	ans = n[:n_length-m_length] + "." + n[n_length-m_length:]
else:
	ans = "0." + "0"*(m_length-n_length) + n

i = -1
while ans[i] == "0":
	i -= 1

if i == -1:
	print(ans)
elif ans[i] == ".":
	print(ans[:i])
else:
	print(ans[:i+1])