# 23hydropathy.py by George Mo

import math
import sys

# Returns Kyte-Doolittle hydrophobicity value for aa residue
# x is aa residue single-letter code

def kdhydro(x):
	if x == 'A': return 1.80
	elif x == 'C': return 2.50
	elif x == 'D': return -3.50
	elif x == 'E': return -3.50
	elif x == 'F': return 2.80
	elif x == 'G': return -0.40
	elif x == 'H': return -3.20
	elif x == 'I': return 4.50
	elif x == 'K': return -3.90
	elif x == 'L': return 3.80
	elif x == 'M': return 1.90
	elif x == 'P': return -1.60
	elif x == 'Q': return -3.50
	elif x == 'R': return -4.50
	elif x == 'S': return -0.80
	elif x == 'T': return -0.70
	elif x == 'V': return 4.20
	elif x == 'W': return -0.90
	elif x == 'Y': return -1.30
	else: return 'Error: Not an aa'

print(KDhydro('A'))
print(KDhydro('D'))
print(KDhydro('W'))
print(KDhydro('X')) # non-aa example