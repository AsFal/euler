this algorithm can be optimized with the knowledge
-all primes cannot have a factor greater than its square root
-all primes can be expressed in the form of 6k+/-1 (except 2 and 3)


def find_nth_prime(n):
    i = 1
    checked_number = 2
    prime_number_list = [2]
    while i != n:
        checked_number +=1
        for j in range(0, len(prime_number_list)):
            if checked_number%prime_number_list[j] == 0:
                break
        else:
            i +=1
            prime_number_list.append(checked_number)
    return checked_number

print find_nth_prime(10001)
