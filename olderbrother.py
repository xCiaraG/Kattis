def get_primes(n):
    table = [True]*n
    primes = [2]*(n//2)
    count = 1                   
    for p in range(3, n, 2):
        if table[p]:    
            primes[count] = p
            count += 1
            for m in range(p*3, n, p*2):
                table[m] = False
    return primes[:count]

n = int(input())
primes = get_primes(int(n**0.5)+1)
i = 0
while i < len(primes):
    if n % primes[i] == 0:
        while n != primes[i] and n % primes[i] == 0:
            n = n // primes[i]
        if n == primes[i]:
            print("yes")
        else:
            print("no")
        break
    i += 1

if n == 1:
    print("no")
elif i == len(primes):
    print("yes")


