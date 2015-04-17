import math


def pretty_print(values):
    for value in values:
        print value


def analyze():
    difference_array = []
    array = []
    with open('report.txt', 'r') as file:
        for line in file:
            # If line contains '---' it's a new list
            if '---' in line:
                difference_array.append(array)
                array = []
            else:
                # Get the absolute value of the difference between
                # the left and the right list
                indic = line.split(',')[3]
                indic = indic.replace('\n', '')
                indic = math.fabs(int(indic))
                array.append(indic)

    # Calculate average
    average_values = []
    for list, i in enumerate(difference_array):
        average_values.append(reduce(lambda x, y: x + y, i) / len(i))

    # Sort average values
    sorted_values = sorted(average_values)
    pretty_print(sorted_values)
