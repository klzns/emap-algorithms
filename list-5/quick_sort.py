def swap(list, i, j):
    if i == j:
        return list
    else:
        prop1 = list.pop(j)
        prop2 = list.pop(i)
        list.insert(i, prop1)
        list.insert(j, prop2)
        return list


def quick(list):
    list_len = len(list)
    if list_len == 0:
        return list

    pivot = list[0]

    if list_len == 1:
        return list
    else:
        j = 1
        for i in range(1, list_len):
            if list[i] < pivot:
                swap(list, j, i)
                j += 1

        swap(list, 0, j-1)
        leftl = len(list[0:j-1])
        rightl = len(list[j:])

        return list, j, leftl, rightl


def quick_sort(list):
    report_file = open('report.txt', 'a')
    if len(list) == 0 or len(list) == 1:
        return list
    else:
        list, j, leftl, rightl = quick(list)
        total = leftl + rightl + 1
        ordered_list = quick_sort(list[0:j-1]) + [list[j-1]] + quick_sort(list[j:])
        if leftl < 3*total/float(4) and rightl < 3*total/float(4):
            bool = 1
        else:
            bool = 0
        text = str(leftl) + "," + str(rightl) + "," + str(total) + "," + str(bool) + "\n"
        report_file.write(text)
        report_file.close()
        return ordered_list
