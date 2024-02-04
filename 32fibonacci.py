# 32fibonacci.py by George Mo

# returns nth value of Fibonacci series

def fibonacci(n):
	n1 = 0
	n2 = 1
	print(n1, end = ' ')
	print(n2, end = ' ')
	for i in range(n):
		nf = n1 + n2
		print(nf, end = ' ')
		n1 = n2
		n2 = nf
	
fibonacci(8)