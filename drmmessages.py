letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

def transfer_sentence(sentence, n):
	s = ""
	for l in sentence:
		s += letters[(letters.index(l)+n)%26]
	return s

def sum_sentence(sentence):
	return sum([letters.index(l) for l in sentence])

def combine_sentences(sentence1, sentence2):
	s = ""
	for i in range(len(sentence1)):
		s += letters[(letters.index(sentence1[i])+letters.index(sentence2[i]))%26]
	return s

sentence = input().strip()
part1, part2 = sentence[:len(sentence)//2], sentence[len(sentence)//2:]
part1, part2 = transfer_sentence(part1, sum_sentence(part1)), transfer_sentence(part2, sum_sentence(part2))
print(combine_sentences(part1, part2))