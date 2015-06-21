class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


def print_status(people, matrix, people_to_remove, iteration):
    print bcolors.BOLD + bcolors.WARNING + str(iteration) + ') Iteration'
    print bcolors.FAIL + 'Removing:'
    print bcolors.ENDC + ', '.join(people_to_remove)
    print bcolors.OKBLUE + bcolors.BOLD + 'List:'
    if len(people) == 0:
        print bcolors.ENDC + '-'
    else:
        print bcolors.ENDC + ', '.join(people) + '\n'


def print_result(people):
    print bcolors.HEADER + '\nFinish!\n'
    print bcolors.OKGREEN + bcolors.BOLD + 'Number of people invited: ' + bcolors.UNDERLINE + str(len(people))
    if len(people) > 0:
        print bcolors.ENDC + ', '.join(people) + '\n'
    else:
        print ''


def print_instructions():
    print '\n----------'
    print bcolors.OKBLUE + 'This script accepts parameters, e.g.:'
    print bcolors.HEADER + '$ python party.py '+ bcolors.BOLD +'<minimum_number_of_friends> <must_unknow_at_least>\n' + bcolors.ENDC
    print bcolors.OKBLUE + 'Using default values of 5 and 5' + bcolors.ENDC
    print '----------\n'
