# Problem 3: The prime factors of 13195 are 5, 7, 13 and 29.

# What is the largest prime factor of the number 600851475143 ?

import math

def find_large_prime(num):
	curr_large = 0
	while num % 2 == 0:
		num /= 2

	new_max_num = math.sqrt(num + 1)
	test_num = 3

	while test_num < new_max_num:
		if num % test_num == 0:
			num /= test_num
			curr_large = test_num
			new_max_num = math.sqrt(num + 1)
		else:
			test_num += 2

		if num is not 1:
			curr_large = num
	return curr_large

print find_large_prime(600851475143)

