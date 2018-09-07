# Here we are rewriting a function that can be found in pb10.py
#This function uses the sieve of Erasthothenes method to find all
# prime numbers in a given interval

from math import sqrt, log

def prime_sieve(lower, upper):

	is_prime_array = [True] * upper
	n = 2

	while n < sqrt(upper):
		if is_prime_array[n]:
			i = 0
			while pow(n,2) + n*i < upper:
				is_prime_array[pow(n,2) + n*i] = False
				i +=1
		n+=1

	prime_array = []
	for i in range(lower, upper):
		if is_prime_array[i]:
			prime_array.append(i)

	return prime_array


# These comments need to be revisited and refactored

# Returns an array containing arrays that have replacement patterns
# for primes between pow(10,n) and pow(10, n+1)

# This function generates ppossibilities for switches for a block of numbers
# Any given block will have numbers between pow(10,n) and pow(10, n+1), meaning 
# they will have n digits in every number

# For example, if n=3. this function will generate swtich possiblities for numbers
# between 100 and 999, which should result in the array
# possibilities = [[0],[1],[0,1],[0,2],[1,2]]

# (A possibility represents the digit placement at which digits will be changed to check the)
# problem's condition
def generate_simultaneous_draws(n):
	# Iterating over the number of numbers we will switch
	possibilities = []

	# This first for loop iterates over all the possibility array's lengths
	# (the number of digits that will be switched at the same time)
	# i is the number of digits that will be switched in the set of generated possibilities
	for i in range(1,n):
		# The while loop iterates over possibilities of i digits until it reaches the last one

		# The starting possibilty is generated with as a and array of size i with each element
		# of the array being a number equal to its index
		possibility = [y for y in range(0,i)]
		print i
		print possibility
		# j represents the index of a number in a possibilty that can no longer be incremented
		# If we take for example i = 3 and n = 4, we should get the resulting possibilities added
		# to the array
		# [0,1,2]
		# [0,1,3]
		# [0,2,3]
		# [1,2,3]
		# By looking at the digits from the right, we can see that once it has reached a maximum
		# value, it can no longer be incremented
		j = i - 1
		while True:
			# print "possibility: " + str(possibility)
			possibilities.append([z for z in possibility])
			# print "return array: " + str(possibilities)
			# This checks if the most right non fixed element of the array has reached its max value
			# If it has, the new modified value will be the one to the left

			has_entered_loop = False
			while possibility[j]== n-(i-j):
				has_entered_loop = True
				j-=1

			possibility[j]+=1

			if has_entered_loop:
				if possibility[j] != possibility[j+1]-1:
					for k in range(j+1,i):
						possibility[k] = possibility[j]+(k-j)
					j = i-1

			# print "1: " + str(possibilities[len(possibilities)-1])
			# print "2: " + str([x for x in range(n-i,n)])
			# print "return array second: " + str(possibilities)
			if possibilities[len(possibilities)-1] == [x for x in range(n-i,n)]:
				break

	return possibilities

def switch_filter(possibilities):
	filtered_positions = []
	for possibility in possibilities:
		if possibility[0] != 0:
			filtered_positions.append(possibility)
	return filtered_positions

			
def generate_first_number(fixed_digits,switch_digits, number_digits):
	constructed_number=0
	number_of_fixed = int(log(fixed_digits,10))
	for digit in range(number_digits-1,-1,-1):
		if digit not in switch_digits:
			constructed_number+= int(fixed_digits/pow(10,number_of_fixed))*pow(10, digit)
			fixed_digits -= (fixed_digits/pow(10,number_of_fixed))*pow(10,number_of_fixed)
			number_of_fixed -= 1
	return constructed_number


# This function wants to find the smallest prime that is a part of 
# an eight digit replacement therapy

# We can't have only the first number change, because that would mean
# that we'd have a maximum of 4 primes (ends in 1,3,7,9)
# #
def replacement_therapy():
	n=0
	while True:
		block = prime_sieve(pow(10,n), pow(10, n+1))
		
		# check_replacemetn
		# We want to look for a 3rd failure, for example
		# We are missing a for loop here inside (for every switch do something)
		switch_positions = generate_simultaneous_draws(n)
		filtered_positions = switch_filter(switch_positions)
		
		for switch_possibility in filtered_positions:
			for i in range(0,pow(10,n-len(switch_possibility))):
				first_hypothetical_prime = generate_first_number(i,switch_possibility,n)
				hypothetical_prime = first_hypothetical_prime
				for j in range(1,10):
					if hypothetical_prime not in block:
						failure_count +=1
						if failure_count == 3:
							first_hypothetical_prime = 0
							break
					for digit in switch_possibility:
						hypothetical_prime += pow(10,digit)

				if first_hypothetical_prime !=0:
					return first_hypothetical_prime
		n+=1
		print "Block " +str(n) + " has failed. "
		# If the for looop ends normally (which would trigger the else
		# statement), that means that some of the possibilities



replacement_therapy()
# print prime_sieve(100, 1000)
# possibilities = generate_simultaneous_draws(4)
# print "unfiltered: " + str(possibilities)
# print "filtered: " + str(switch_filter(possibilities))
# print "generated number" + str(generate_first_number(876,[1,2],5))