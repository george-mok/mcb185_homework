# 36poisson.py by George Mo

import math

# n = expectation and k = events

# Factorial function

def factorial(n):
	if n == 0: return 1
	fact = 1
	for i in range(1, n+1):
		fact = fact * i
	return fact

# Poisson probability 	

def poisson(n, k):
	prob = ((n**k) * (math.e**((-1) * n))) / factorial(k)
	return prob
	
print(poisson(3, 4))
print(poisson(5, 10))
print(poisson(18, 39))
print(poisson(8, 2))