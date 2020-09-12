import sys

def jobSequencing(P, Q, n):

	slots = [False] * n

	# P.sort(reverse=True)
	P_sorted = sorted(enumerate(P), reverse=True, key=lambda x: x[1])

	for record in P_sorted:

		p, d = record[1], Q[record[0]]

		for j in range(len(slots)-1, -1, -1):

			if j <= d and slots[j-1] == False:

				slots[j-1] = record[1]

				break

	return slots

if __name__ == '__main__':

	P = [10, 20, 15, 1, 5]
	Q = [1, 2, 2, 3, 3]

	print('Profit: ', P)
	print('Deadline: ', Q)

	n = max(Q)

	seq = jobSequencing(P, Q, n)

	print('The job sequencing is: ', seq)
	print('The max profit is: ', sum(seq))

