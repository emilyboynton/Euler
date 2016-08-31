def check(num):
	num = str(num)
	limit = (len(num)+1)/2
	for i in range(0, limit):
		if num[i] == num[-1-i]:
			continue
		else:
			return False
	return True

print check(98089)


def find_largest():
	largest = 0
	for i in range(100, 999):
		for j in range(100, 999):
			if check(i*j) and i*j > largest:
				largest = i*j
	print largest 


find_largest()