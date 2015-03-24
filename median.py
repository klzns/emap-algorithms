import random

s = [2, 36, 5, 21, 8, 13, 11, 20, 5, 4, 1]


def median(s):
	sl = []
	sv = []
	sr = []
	v = random.randint(0, len(s))

	for number in s:
		if number < v:
			sl.append(number)
		elif number is v:
			sv.append(number)
		else:
			sr.append(number)

	return len(sl), len(sr)

if __name__ == '__main__':
	size_l, size_r = median(s)
	print "Size of the left side: " + str(size_l)
	print "Size of the left right: " + str(size_r)

	if size_r is 5 or size_r is 6:
		print "Good choice!"