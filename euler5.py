# 2520 is the smallest number that can be 
# divided by each of the numbers from 1 to 10 without any remainder.

# What is the smallest positive number that is 
# evenly divisible by all of the numbers from 1 to 20?

def smallest_num(step):

	num_to_check = step

	flag = False
	while not flag:
		flag = check(num_to_check, step)
		if not flag:
			num_to_check += step

	print num_to_check


def check(num_to_check, step):

	for i in range(1, step):
		if num_to_check % i != 0:
			return False

	return True

smallest_num(20)
