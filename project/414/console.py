
class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


def print_graph(graph):
    print bcolors.BOLD + 'Graph data:' + bcolors.ENDC
    for v in graph:
        for w in v.get_connections():
            vid = v.get_id()
            wid = w.get_id()
            print('( ' + bcolors.OKBLUE + str(vid) + bcolors.ENDC + ', ' +
                  bcolors.OKGREEN + str(wid) + bcolors.ENDC + ', ' +
                  bcolors.WARNING + str(v.get_weight(w))+bcolors.ENDC+' )')


def print_dijkstra():
    print bcolors.BOLD + "\nDijkstra's shortest path" + bcolors.ENDC


def print_update(current, next, distance):
    print(bcolors.HEADER + 'Updated:\t' + bcolors.ENDC +
          ' current = ' + bcolors.OKBLUE + current + bcolors.ENDC +
          ', next = ' + bcolors.OKGREEN + next + bcolors.ENDC +
          ', new dist = ' + bcolors.WARNING + str(distance) + bcolors.ENDC)


def print_not_updated(current, next, distance):
    print(bcolors.FAIL + 'Not updated:\t' + bcolors.ENDC +
          ' current = ' + bcolors.OKBLUE + current + bcolors.ENDC +
          ', next = ' + bcolors.OKGREEN + next + bcolors.ENDC +
          ', new dist = ' + bcolors.WARNING + str(distance) + bcolors.ENDC)


def print_path(path):
    print bcolors.BOLD + '\nThe shortest path: ' + bcolors.OKBLUE
    print path[::-1]
    print bcolors.ENDC


def print_instructions():
    print '\n----------'
    print bcolors.OKBLUE + 'This script accepts parameters, e.g.:'
    print(bcolors.HEADER + '$ python passing.py ' + bcolors.BOLD +
          '<v0> <from> <to>\n' + bcolors.ENDC)
    print(bcolors.OKBLUE + "Using default values of 'a', 'd' and 'c'" +
          bcolors.ENDC)
    print '----------\n'
