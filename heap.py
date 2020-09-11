# Below program will create a max-heap for an array

import math
import sys


def heapify(arr, n, i):
	
	largest = i

	l = 2 * i + 1
	r = 2 * i + 2

	if l < n and arr[largest] < arr[l]:
		largest = l

	if r < n and arr[largest] < arr[r]:
		largest = r

	if largest != i:
		
		arr[i], arr[largest] = arr[largest], arr[i]
		heapify(arr, n, largest)

def buildHeap(arr, n):

	last_nonleaf_node = n // 2 - 1

	for i in range(last_nonleaf_node, -1, -1):
		heapify(arr, n, i)


if __name__ == '__main__':

	# arr = [4, 10, 3, 5, 1]

	arr = [1, 3, 5, 4, 6, 13, 10, 9, 8, 15, 17]

	print('Before heap: ', arr)

	n = len(arr)

	buildHeap(arr, n)

	print('After heap: ', arr)
	
