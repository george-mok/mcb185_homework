# 22oligotemp by George Mo

import math
import sys

def oligo(a, c, g, t): # n = number of nt in oligo
	n = a + c + g + t
	if n <= 13: 	return (a + t)*2 + (c + g)*4
	if n > 13:		return 64.9 + 41*(c + g - 16.4)/(a + c + g + t)

print(oligo(5, 5, 5, 5)) 	# n > 13
print(oligo(1, 1, 1, 1)) 	# n < 13
print(oligo(6, 10, 12, 20))
print(oligo(20, 10, 15, 12))