'''
There are different pieces of number theory that we can use to create a more
efficient algorithm to solve this problem.

1. When checking for divisors, we will consider two types of numbers, squares
and non-squares.
-Squares have a number of divisors equal to 2n+1
-Non-squares have a number of divisors equal to 2n
where in both cases n is the number of divisors found before the root of the
verified nuumber

2. The nth triangular number can be found using this formula

Tn = n*(n+1)/2

3. Given a whole number c where c is the product of whole numbers a and b,
c has a number of divisors equal to the product of the number of divisors of
a and b.

From this information we can conclude that the number of divisors for a given
triangular number can be foudn using this equation:

Dn = o*(e-1)
-> only the case when e is a power of 2
Dn = o*(e-2)
->The case for most other scenarios

These equations are only true when the two considered numbers are coprimes,
else the number of factors of a number can be found by finding the prime factors
Given a number n who is the product of powers of the  prime factors a,b,c

n = pow(a,k)*pow(b,l)*pow(c,m)
n has a number of divisors d equal to

d = (k+1)*(l+1)*(m+1)

(Although, the above formula could create a bound for the number of divisors
(this need to be proved))

where o is the odd numerator in equation two and e is the even numerator in
equation 2
'''
from math import sqrt, ceil
# from functions import add_to_library


# We want this function to map out the number of prime factors to the prime factors
def split_into_prime_factors(number):
    n=2
    lib = {}
    temp = number
    while n <= sqrt(number):
        i = 0
        while temp%n == 0:
            temp/=n
            i+=1
        else:
            if n != 0:
                lib[n] = i
        n+=1
    print lib
    return lib


#We want this function to be a more efficient way to find the nuber of divisors, 
#using the prime technique
def number_of_divisors(number):
    n=2
    divisors = 1
    temp = number
    while n <= number:
        i = 0
        while number%n == 0:
            number/=n
            i +=1
        else:
            divisors *= (i+1)
        n+=1
    return divisors


def triangular_number_at(n):
    return n*(n+1)/2

def find_first_triangular_number_with_n_divisors(min_divisors):
    n=2

    while True:
        triangular_number = triangular_number_at(n)
        if number_of_divisors(triangular_number)>min_divisors:
            return triangular_number
        n+=1

num = find_first_triangular_number_with_n_divisors(500)
print "first t number is" + str(num)
# num = find_first_triangular_number_with_n_divisors(500)
print num

