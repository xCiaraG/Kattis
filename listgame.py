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
primes = get_primes(int(n**(.5))+1)
length = len(primes)
count = 0
while n != 1:
    i = 0
    while i < length and primes[i] <= n and n % primes[i] != 0:
        i += 1
    if i == length or primes[i] >= n:
        n = 1
    else:
        n = n // primes[i]
    count += 1
print(count)