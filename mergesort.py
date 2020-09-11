# below code performs a merge sort operation on an array		
def mergeSort(arr):

	# Step 1: Divide array in 2 list recursively until smallest array
	if len(arr) > 1:
		mid = len(arr) // 2
		L = arr[:mid]
		R = arr[mid:]
		# print('left call...', L)
		mergeSort(L)
		# print('right call...', R)
		mergeSort(R)
		
		i = 0
		j = 0
		k = 0

		# Step 2: Merge smallest 2 list
		while i < len(L) and j < len(R):
			if L[i] < R[j]:
				arr[k] = L[i]
				i += 1
			else:
				arr[k] = R[j]
				j += 1
			k += 1
		
		## copy remaining elements
		while i < len(L):
			arr[k] = L[i]
			k += 1
			i += 1
		while j < len(R):
			arr[k] = R[j]
			k += 1
			j += 1

if __name__ == '__main__':

	arr = [3,4,2,77,5,13,8,10]
	
	print('original : ', arr)

	mergeSort(arr)

	print('sorted : ', arr)
