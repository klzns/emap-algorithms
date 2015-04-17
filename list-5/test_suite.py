import random
import sys
from quick_sort import quick_sort, quick
from analysis import analyze


def generate_random_list(size):
    return random.sample(xrange(size), size)


def run(M):
    # Quick sort a list of M elements
    list = generate_random_list(M)
    quick_sort(list)

    # Separate each run with a line with '---'
    report_file = open('report.txt', 'a')
    report_file.write('---\n')
    report_file.close()


def run_n_times(M, N):
    # Run N times
    for i in range(N):
        run(M)


if __name__ == '__main__':
    if len(sys.argv) is 3:
        M = sys.argv[1]
        N = sys.argv[2]
        report_file = open('report.txt', 'w')
        run_n_times(int(M), int(N))
        print '\nPercent of good pivots for each run sorted by the worst case:\n'
        analyze()
        print ''
    else:
        print 'Type the arguments for M (size of the list) and N (times to run)'
        print 'Ex: python test_suite.py 3 2'
