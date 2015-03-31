import random

s = [2, 36, 5, 21, 8, 13, 11, 20, 5, 4, 1]

s = [3, 1, 2]

def median(s):
	sl = []
	sv = []
	sr = []
	random_index = random.randint(0, len(s)-1)
	v = s[random_index]
	v = 2
	print v

	start_lesser = 0
	end_lesser = 0
	greater = len(s) - 1
	start_same = None
	end_same = None

	work = True
	steps = 0
	while work:
		steps = steps + 1
		number = s[end_lesser]
		if number < v:
			print number, ' < ', v
			end_lesser = end_lesser + 1
			print s
			print ''
		elif number is v:
			print number, ' == ', v
			if end_lesser+1 > len(s)-1:
				break
			if v > s[end_lesser+1]:
				temp = s[end_lesser]
				s[end_lesser] = s[end_lesser+1]
				s[end_lesser+1] = temp
			else:
				start_lesser = start_lesser + 1
				end_lesser = end_lesser + 1
			print s
			print ''
		elif number > v:
			print number, ' > ',  v
			if greater is end_lesser:
				greater = greater - 1
				break
			else:
				temp = s[end_lesser]
				s[end_lesser] = s[greater]
				s[greater] = temp
				greater = greater - 1
			print s
			print ''


	print s
	print 'Steps: ', steps, ' of ', len(s)
	return end_lesser - start_lesser, len(s)-1 - greater

def is_a_good_median(s, size_l, size_r):
	range_of_goodness = len(s)*3/4

	if range_of_goodness > size_l and\
		range_of_goodness > size_r:
		print "Good choice!"

if __name__ == '__main__':
	size_l, size_r = median(s)
	print "Size of the left side: " + str(size_l)
	print "Size of the right side: " + str(size_r)

	is_a_good_median(s, size_l, size_r)
