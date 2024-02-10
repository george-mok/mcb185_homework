# 40demo.py by George Mo

import random
import sys

for i in range(5):
	print(random.choice('ACGT'), end='')
print()

for i in range(5):
	print(random.gauss(0.0, 1.0))
	
#print('this line\n has some\n line breaks')
#print('a\tb\tcat\tdogma')
print(100, 2000, 30000, 40000, sep = '\t')

"""
i = 1
pi = 3.14159
print('normal string {i} {pi}')
print(f'formatted string {i} {pi}')
print(f'tau {pi + pi}')
print(f'formatted string {i} {pi:.3f}')
"""

#print('logging', file=sys.stderr)

random.seed(1)
print(random.random())
print(random.random())
random.seed(2)
print(random.random())
print(random.random())