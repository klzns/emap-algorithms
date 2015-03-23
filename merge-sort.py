from collections import deque

list = [5, 2, 69, 21, 123, 1, 4]


def merge(list_a, list_b):
	if len(list_a) is 0:
		return list_b	
	if len(list_b) is 0:
		return list_a

	if list_a[0] < list_b[0]:
		return [list_a[0]] + list_a[1:] + list_b[:]
	else:
		return [list_b[0]] + list_a[:] + list_b[1:]


def merge_sort(list):
	queue = deque([])

	for i in range(0, len(list)):
		queue.append([list[i]])

	while len(queue) > 1:
		queue.append(merge(queue.popleft(), queue.popleft()))

	return queue.popleft()

if __name__ == '__main__':
	print merge_sort(list)

