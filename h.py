import sys
lines = []
for highest_prime_index in sys.stdin:
    lines.append(highest_prime_index.strip())

firstline_numbers = [int(s) for s in lines[0].split(' ')]
# print(firstline_numbers)

start_index = firstline_numbers[0] - 1
end_index = firstline_numbers[1] - 1
substring = lines[1]
# print(substring)

primes = [2]
test_number = 3
highest_prime_index = 0
count = 0
if substring in '2':
    count += 1
while highest_prime_index <= end_index:
    # print('starting', n)
    isprime = True
    for prime in primes:
        if prime > test_number**0.5:
            break
        if test_number%prime == 0:
            isprime = False
            break
    if isprime:
        primes.append(test_number)
        highest_prime_index+=1
        if start_index <= highest_prime_index and substring in str(test_number):
            count += 1
    test_number+=2
# print(primes[:20])
print(count)
    


