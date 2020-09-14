import numpy as np

if __name__ == '__main__':

	p = [0,1,2,5,6]
	wt = [0,2,3,4,5]

	print('The inputs are: ', wt)

	n = 4 # no. of items
	m = 8 # total capacity

	k = np.zeros((n+1, m+1))

	for i in range(1, n+1):

		for w in range(1, m+1):

			if wt[i] <= w:

				k[i][w] = max( k[i-1][w], p[i] + k[i-1][w-wt[i]] )
			else:
				k[i][w] = k[i-1][w]

	print('The tabular calculation is as below:')
	print(k)

	i = n
	j = m

	res = []

	while i > 0 and j > 0:
		if k[i][j] == k[i-1][j]:
			print('{} = 0'.format(i))
			i -= 1
		else:
			print('{} = 1'.format(i))
			res.append(wt[i])
			j = j - wt[i]
			i -= 1

	print('The choosen weights are:', res)
