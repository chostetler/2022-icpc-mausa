i = 0
n = 3
primes = [2]
substring = '9'
while i < 10**5 + 10:
    # print('starting', n)
    isprime = True
    for prime in primes:
        if prime > n**0.5:
            break
        if n%prime == 0:
            isprime = False
            break
    if isprime:
        primes.append(n)
        # print('adding prime', n, primes)
        i+=1
    n+=2
print(','.join([str(p) for p in primes]))
    

