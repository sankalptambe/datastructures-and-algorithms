# fibonacci series
# find series upto n number.

import sys

n = int(input('Please provide a number: '))


# Fibonacci Series using Dynamic Programming  
def fibonacci(n):  
      
    # Taking 1st two fibonacci nubers as 0 and 1  
    FibArray = [0, 1]  
      
    while len(FibArray) < n + 1:  
        FibArray.append(0)  
      
    if n <= 1:  
        return n  
    else:  
        if FibArray[n - 1] == 0:  
            FibArray[n - 1] = fibonacci(n - 1)  
  
        if FibArray[n - 2] == 0:  
            FibArray[n - 2] = fibonacci(n - 2)  
              
    FibArray[n] = FibArray[n - 2] + FibArray[n - 1]  
    return FibArray[n]  

###################

def printFib(n):
	if n <= 0:
		return 0
	if n == 1:
		return n
	
	fib_arr = [0, 1]
	
	n1 , n2 = fib_arr

	for count in range(2, n):
		
		nth = n1 + n2
		
		fib_arr.append(nth)

		n1 = n2
		n2 = nth

	return fib_arr

#####################

print('input is:', n)

print('{}th in fibonacci sequence is : '.format(n) , fibonacci(n) )

print('Fibonacci series upto {} th number is : {}'.format(n, ' '.join([str(el) for el in printFib(n)])))

