# 25entropy.py by George Mo

import math
import sys

#Given counts of A's, C's, G's, T's, returns Shannon entropy value

def shannon(a, c, g, t):
	pa = a/(a + c + g + t)
	if a == 0: pa1 = 0
	else: pa1 = pa * math.log2(pa)
	pc = c/(a + c + g + t)
	if c == 0: pc1 = 0
	else: pc1 = pc * math.log2(pc)
	pg = g/(a + c + g + t)
	if g == 0: pg1 = 0
	else: pg1 = pg * math.log2(pg)
	pt = t/(a + c + g + t)
	if t == 0: pt1 = 0
	else: pt1 = pt * math.log2(pt)
	return -1 * (pa1 + pc1 + pg1 + pt1)
	
print(shannon(10, 10, 30, 30))
print(shannon(0, 10, 30, 30))
print(shannon(10, 0, 30, 30))
print(shannon(10, 10, 0, 30))
print(shannon(10, 10, 30, 0))