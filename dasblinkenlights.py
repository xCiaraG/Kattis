def find_crossover(p, q, s):
  for i in range(1, s + 1):
    if (i % p == 0) and (i % q == 0):
      return 'yes'
  return 'no'

p, q, s = [int(x) for x in input().split()]
print(find_crossover(p, q, s))