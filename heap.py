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

	# looping from last nonleaf node to root node.
	for i in range(last_nonleaf_node, -1, -1):
		heapify(arr, n, i)

# main function to do heap sort  
def heapSort(arr, n): 
      
    # Build heap (rearrange array)  
    buildHeap(arr, n)

    print('Heapify: ', arr)

    # One by one extract an element from heap  
    for i in range(n-1, -1, -1): 
          
        # Move current root to end # 
        arr[0], arr[i] = arr[i], arr[0] 
  
        # call max heapify on the reduced heap  
        heapify(arr, i, 0) 

if __name__ == '__main__':

	# arr = [4, 10, 3, 5, 1]

	arr = [1, 3, 5, 4, 6, 13, 10, 9, 8, 15, 17]

	print('Original: ', arr)

	n = len(arr)

	heapSort(arr, n)

	print('Heapsort: ', arr)
	
