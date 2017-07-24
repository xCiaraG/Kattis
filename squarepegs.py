import math
line = input()
plots = list(map(int, input().strip().split()))
circular = list(map(int, input().strip().split()))
square = list(map(int, input().strip().split()))
house = circular[:]
for h in square:
   house.append((math.sqrt((h**2)+(h**2)))/2)
house = sorted(house)
plots = sorted(plots)
count = 0
while house and plots:
   if house[-1] < plots[-1]:
      house = house[:-1]
      plots = plots[:-1]
      count += 1
   else:
      house = house[:-1]
print(count)