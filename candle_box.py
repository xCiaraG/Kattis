difference = int(input())
rita = int(input())
theo = int(input())
tmp_rita = 0
tmp_theo = 0
rita_age = 4
theo_age = rita_age - difference
while tmp_theo + tmp_rita != rita + theo:
	tmp_rita += rita_age
	if theo_age > 2:
		tmp_theo += theo_age
	theo_age += 1
	rita_age += 1

print(rita - tmp_rita)