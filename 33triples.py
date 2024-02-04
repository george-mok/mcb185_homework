# 33triples.py by George Mo

import math

a = 1
b = 1

for a in range(1, 100):
	for b in range(a + 1, 100):
		c = ((a**2 + b**2)**0.5)
		if c % 1 == 0:
			print(a, b, c)