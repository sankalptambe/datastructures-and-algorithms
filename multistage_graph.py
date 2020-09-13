# multistage graph. 
## Applications eg: Resource allocation

# Find out the shortest distant path from source 1 to 8

import sys

if __name__ == '__main__':

	stages = 4
	n = 8

	arr = [	#0,1,2,3,4,5,6,7,8
			[0,0,0,0,0,0,0,0,0], #0
			[0,0,2,1,3,0,0,0,0], #1
			[0,0,0,0,0,2,3,0,0], #2
			[0,0,0,0,0,6,7,0,0], #3
			[0,0,0,0,0,6,8,9,0], #4
			[0,0,0,0,0,0,0,0,6], #5
			[0,0,0,0,0,0,0,0,4], #6
			[0,0,0,0,0,0,0,0,5], #7
			[0,0,0,0,0,0,0,0,0], #8

	] 

	cost = [0]*(n+1)
	d = [0]*(n+1)

	# stages = 4
	path = [0]*(stages+1)

	# step 1: start from last node to 1st node
	for i in range(n-1, -1, -1):

		min = 32767

		for j in range(i+1, n+1):

			if arr[i][j] != 0 and arr[i][j] + cost[j] < min:

				min = arr[i][j] + cost[j]
				d[i] = j

		cost[i] = min

	# print('cost:', cost)
	# print('d: ', d)

	print('minimum distance from source 1 to 8 is: ', cost[1])

	# step 2: forward propogate to find shortest path
	path[1] = 1
	path[4] = 8

	for i in range(2, stages):
		path[i] = d[path[i-1]]

	# print(path)

	path.pop(0)

	print('path taken from source 1 to 8 is: ', ' '.join([str(el) for el in path]) )