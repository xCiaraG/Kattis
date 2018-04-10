from sys import stdin

def get_primes(n):
   table = [0, 0, 1] + [1, 0]*((n-2)//2)
   for p in range(3, int(n**(0.5)) + 1, 2):
      if table[p]:    
         for m in range(p*2, n, p):
            table[m] = 0
   return table

def find_factors(p, a, b):
   if a % p == 0:
      return set([i for i in range(a, b + 1, p)])
   else:
      return set([i for i in range(a + (p - (a % p)), b + 1, p)])

tmp_primes = get_primes(1000)
tmp_primes = [i for i in range(1000) if tmp_primes[i]]
n = int(input())
for k in range(n):
   a, b, p = [int(x) for x in stdin.readline().split()]
   i = 0
   while i < len(tmp_primes) and tmp_primes[i] < p:
      i += 1
   primes = tmp_primes[i:]
   factors = []
   for p in primes:
      f = find_factors(p, a, b)
      if f:
         factors.append(f)
   i = 0
   while i < len(factors):
      changed = False
      j = i + 1
      while j < len(factors):
         tmp = factors[i].intersection(factors[j])
         if tmp:
            factors[i] = factors[i].union(factors[j])
            factors = factors[:j] + factors[j+1:]
            changed = True
         else:
            j += 1
      if not changed:
         i += 1
   ans = b - a + 1
   for f in factors:
      ans -= (len(f) - 1)
   print("Case #{}: {}".format(k + 1, ans))