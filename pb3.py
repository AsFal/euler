def find_highest_prime_factor(multiple):
    temp = multiple
    test_factor = 2
    max_factor = test_factor

    while test_factor <= temp:
        while temp%test_factor == 0:
            max_factor = test_factor
            temp /= test_factor
        test_factor +=1
    return max_factor

print find_highest_prime_factor(600851475143)
