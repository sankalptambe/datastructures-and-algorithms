# find all the shortest path for all the vertices

## for a single source we can use Dijkstra algorithm 
## for which time complexity is O(n).
## for all pairs of shortest paths we can find in O(n3) complexity.

import sys
import numpy as np

if __name__ == '__main__':

	n = 4

	edges = [(1,2), (1,4), (2,1), (2,3), (3,1), (3,4),(4,1)]

	weights = [3, 7, 8, 2, 5, 1, 2]

	arr = (np.ones((n,n)) * np.inf)

	np.fill_diagonal(arr, 0)

	for idx, edge in enumerate(edges):

		arr[edge[0]-1][edge[1]-1] = weights[idx]

	print('Adjacent matrix for given edges: ')
	print(arr)

	for k in range(n):

		for i in range(n):

			for j in range(n):

				# print(arr[i][j], arr[i][k], arr[k][j])
				arr[i][j]  = min(arr[i][j], arr[i][k] + arr[k][j])
			

	print('All pairs for shortest path: ')
	print(arr)

