import math
import sys

def partition(arr, l, h):

	i = l
	j = h

	pivot = arr[l]

	while i < j:

		i += 1
		while arr[i] <= pivot:
			i += 1

		while arr[j] > pivot:
			j -= 1

		if i < j :
			arr[i], arr[j] = arr[j] , arr[i]

	arr[l], arr[j] = arr[j], arr[l]

	return j	

def quicksort(arr, l, h):
	
	if len(arr) == 1:
	        return arr
	
	if l < h:

		j = partition(arr, l, h)

		quicksort(arr, l, j)
		quicksort(arr, j+1, h)

if __name__ == '__main__':

	arr = [10, 16, 8, 12, 15, 6, 3, 9, 5]

	print('Original: ', arr)

	arr.append(math.inf)

	quicksort(arr, 0, len(arr) - 1)

	arr.pop()
	
	print('Quicksort: ', arr)
