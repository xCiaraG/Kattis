from sys import stdin

string_to_numbers = {"xxxxxx...xx...xx...xx...xx...xxxxxx" : "0", 
		  			 "....x....x....x....x....x....x....x" : "1", 
		   			 "xxxxx....x....xxxxxxx....x....xxxxx" : "2", 
		   			 "xxxxx....x....xxxxxx....x....xxxxxx" : "3", 
		   			 "x...xx...xx...xxxxxx....x....x....x" : "4", 
		   			 "xxxxxx....x....xxxxx....x....xxxxxx" : "5", 
		   			 "xxxxxx....x....xxxxxx...xx...xxxxxx" : "6", 
		   			 "xxxxx....x....x....x....x....x....x" : "7",
		   			 "xxxxxx...xx...xxxxxxx...xx...xxxxxx" : "8", 
		   		     "xxxxxx...xx...xxxxxx....x....xxxxxx" : "9", 
		   			 ".......x....x..xxxxx..x....x......." : "plus"}

numbers_to_string = {"0" : "xxxxxx...xx...xx...xx...xx...xxxxxx", 
		  			 "1" : "....x....x....x....x....x....x....x", 
		   			 "2" : "xxxxx....x....xxxxxxx....x....xxxxx", 
		   			 "3" : "xxxxx....x....xxxxxx....x....xxxxxx", 
		   			 "4" : "x...xx...xx...xxxxxx....x....x....x", 
		   			 "5" : "xxxxxx....x....xxxxx....x....xxxxxx", 
		   			 "6" : "xxxxxx....x....xxxxxx...xx...xxxxxx", 
		   			 "7" : "xxxxx....x....x....x....x....x....x",
		   			 "8" : "xxxxxx...xx...xxxxxxx...xx...xxxxxx", 
		   		     "9" : "xxxxxx...xx...xxxxxx....x....xxxxxx", 
		   			 "plus" : ".......x....x..xxxxx..x....x......."}

line = stdin.readline().strip()
nums = [""]*((len(line)//6)+1)
for i in range(0, 7):
	for j in range(0, len(line), 6):
		nums[j//6] += line[j:j+5]
	line = stdin.readline().strip()

num = ""
for i in range(0, len(nums)):
	num += string_to_numbers[nums[i]]
n1, n2 = num.split("plus")
ans = str(int(n1) + int(n2))

for i in range(0, 7):
	s = ""
	for c in ans:
		s += numbers_to_string[c][i*5:(i*5)+5] + "."
	print(s[:-1])