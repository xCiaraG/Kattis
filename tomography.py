line = input()
rows = [int(x) for x in input().split()]
columns = [int(x) for x in input().split()]
tmp_rows = rows[:]
tmp_columns = columns[:]

for n in rows:
	tmp_columns = sorted(tmp_columns, reverse=True)
	for i in range(0, n):
		tmp_columns[i] -= 1
	if -1 in tmp_columns:
		break

for n in columns:
	tmp_rows = sorted(tmp_rows, reverse=True)
	for i in range(0, n):
		tmp_rows[i] -= 1
	if -1 in tmp_rows:
		break

if -1 in tmp_columns or -1 in tmp_rows:
	print("No")
else:
	print("Yes")