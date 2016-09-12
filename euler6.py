# The sum of the squares of the first ten natural numbers is,
# 1^2 + 2^2 + ... + 10^2 = 385
# The square of the sum of the first ten natural numbers is,
# (1 + 2 + ... 100)^2 = 552 = 3025
# Hence the difference between the sum of the squares and the
# square of the sum is 3025 - 385 = 2640

# Find the difference between the sum of the squares of the 
# first one hundred natural numbers and the square of the sum


def diff_square_sum(num):
	sum_square = 0
	squares = 0

	for i in range(1, num + 1):
		sum_square += i
	sum_square *= sum_square


	for i in range(1, num + 1):
		squares += i*i

	return sum_square - squares


print diff_square_sum(100)