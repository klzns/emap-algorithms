import random

s = [2, 36, 5, 21, 8, 13, 11, 20, 5, 4, 1]


def median(s):
    sl = []
    sv = []
    sr = []
    random_index = random.randint(0, len(s)-1)
    v = s[random_index]

    for number in s:
        if number < v:
            sl.append(number)
        elif number is v:
            sv.append(number)
        else:
            sr.append(number)

    return len(sl), len(sr)


def is_a_good_median(s, size_l, size_r):
    range_of_goodness = len(s)*3/4

    if range_of_goodness > size_l and\
       range_of_goodness > size_r:
        print "Good choice!"

if __name__ == '__main__':
    size_l, size_r = median(s)
    print "Size of the left side: " + str(size_l)
    print "Size of the left right: " + str(size_r)

    is_a_good_median(s, size_l, size_r)
