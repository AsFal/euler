# using the sieve of Eratosthenes

# make it into a dictionary so that we access
# the marking with the keys
from collections import defaultdict


def find_primes_up_to(number):
    prime_list = [2]
    p = prime_list[0]
    marked_numbers = defaultdict(lambda:'u')
    while p < number:
        n = 2
        while n*p < number:
            marked_numbers[n*p] = 'm'
            n +=1
        # simulate a do-while loop
        p +=1
        while p < number:
            if marked_numbers[p] == 'u':
                prime_list.append(p)
                break
            p +=1

    return prime_list

prime_list = find_primes_up_to(2000000)
sum = 0
for prime in prime_list:
    sum += prime

print sum
