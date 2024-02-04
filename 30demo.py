# 30demo.py by George Mo

import math

"""
i = 1
while i < 10:
	print(i)
	i = i + 3
print('final value of i is', i)
"""

"""for i in range(0, 5):
	print(i)
print('final value of i is', i)"""
# equivalent to: for i in range(5): print(i)
# default lower bound = 0 and default step = 1

"""seq = 'GAATTC'
for nt in seq:
	print(nt)
"""
"""
for nt1 in 'ACGT':
	for nt2 in 'ACGT':
		if nt1 == nt2: print(nt1, nt2, '+1')
		else:          print(nt1, nt2, '-1')
"""

#now abstract out 'ACGT'

nts = 'ACGT'
"""
for nt1 in nts:
	for nt2 in nts:
		if nt1 == nt2: print(nt1, nt2, '+1')
		else:          print(nt1, nt2, '-1')
		
"""

"""
limit = 4
for i in range(0, limit):
	for j in range(i + 1, limit):
		print(i + 1, j + 1)
"""

"""def gc_comp(seq):
	gc_count = 0
	total = 0
	for nt in seq:
		if nt == 'C' or nt == 'G':
			gc_count = gc_count + 1
		total = total + 1
	return gc_count / total

print(gc_comp('ACAGCGAAT'))"""

# Triangular numbers

def triangular(n):
	tri = 0
	for i in range(n+1):
		tri = tri + i
	return tri
print(triangular(4))

# Factorials

def factorial(n):
	if n == 0: return 1
	fact = 1
	for i in range(1, n+1):
		fact = fact * i
	return fact
print(factorial(4))

# Euler's number

def euler(limit):
	e = 0
	for n in range(limit):
		e = e + 1 / factorial(n)
	return e
print(euler(5))

# Perfect Squares

def is_perfect_square(n):
	root = math.sqrt(n)
	if math.isclose(root, root // 1): return True
	return False
print(is_perfect_square(24))

# Prime Numbers

def is_prime(n):
	for den in range(2, n//2): # first factor is divide by 2
		if n % den == 0: return False """tests if can be factored further
		                              out of numbers leading up to n // 2"""
	return True
print(is_prime(9818))