# 50demo.py by George Mo

import math
import gzip

'''
seq = 'GAATTC'
print(seq[0], seq[1])
print(seq[-1])

for i in range(len(seq)):
	print(i, seq[i])
'''

'''
s = 'ABCDEFGHIJ'
print(s[0:8:2])
print(s[:5])
print(s[5:])           # [5:len(s)] = s[5:]
'''

# Also, s[0] = s[0:1]; think about it--1 is like range "limit"
# s = s[0:len(s)] = s[::]

# print(s, s[::], s[::1], s[::-1])

# Tuples
"""
tax = ('Homo', 'sapiens', 9606)
print(tax)
print(tax[0])
print(tax[::1])

def quadratic(a, b, c):
	if b**2 - 4*a*c < 0:
		return 'None, None'
	if b**2 - 4*a*c == 0:
		x = (((-1)*b) + math.sqrt((b**2) - 4*a*c)/(2*a))
		return x, x
	if b**2 - 4*a*c > 0:
		x1 = (((-1)*b) - math.sqrt((b**2) - 4*a*c)/(2*a))
		x2 = (((-1)*b) + math.sqrt((b**2) - 4*a*c)/(2*a))
		return (x1, x2)

x1, x2 = quadratic(5, 6, 1)
print(x1, x2)

intercepts = quadratic(5, 6, 1)       # DON'T do this, unpack tuple into individual variables
print(intercepts[0], intercepts[1])
"""

"""
nts = 'ACGT'
for i, nt in enumerate(nts):
	print(i, nt)
	
names = ('adenine', 'cytosine', 'guanine', 'thymine')
for nt, name in zip(nts, names):
	print(nt, name)

for i, (nt, name) in enumerate(zip(nts, names)):
	print(i, nt, name)
"""
	
# Lists

"""
nts = ['A', 'T', 'C']
# print(nts)
nts[2] = 'G'
# print(nts)
nts.append('C')
# print(nts)
last = nts.pop()
# print(last)
nts.sort()
print(nts)
"""

"""
# minimum

testlist = [1, 3, 5, 7, 8, 13, 28]

def minimum(vals):
	mini = vals[0]
	for val in vals[1:]:
		if val < mini: mini = val
	return mini

print(minimum(testlist))

# minmax

def minmax(vals):
	mini = vals[0]
	maxi = vals[0]
	for val in vals:
		if val < mini: mini = val
		if val > maxi: maxi = val
	return mini, maxi

print(minmax(testlist))

# mean

def mean(vals):
	total = 0
	for val in vals: total += val
	return total / len(vals)
	
print(mean(testlist))

# entropy

def entropy(probs):
	h = 0
	for p in probs:
		if p == 0: h = 0
		else:      h -= p * math.log2(p)
	return h
	
print(entropy([0, 0.3, 0.5]))

# Kullback-Leibler distance

def dkl(P, Q):
	d = 0
	for p, q in zip(P, Q):
		d += p * math.log2(p/q)
	return d
p1 = (0.4, 0.3, 0.2, 0.1)
p2 = (0.1 , 0.3, 0.4, 0.2)
print(dkl(p1, p2))
"""

"""
with open(path) as fp:           # general structure for reading file lines
	for line in fp:
		function(line)
"""

"""
with gzip.open(path, 'rt') as fp:   # Same as "gunzip -c path"
	for line in fp:
		print(line, end=''	
"""

# numbers in files are strings, must first convert to ints or floats	
i = int ('42')
x = float('0.61803')
print(i, x)


testlist = [1, 5, 3, 7, 8, 13]

def median(vals):
	middle = (len(vals) / 2) - 1
	int(middle)
	print(middle, type(middle))
	
def mean(vals):
	total = 0
	for val in vals: total += val
	return total / len(vals)
	
print(mean(testlist))
testlist.sort()
print(testlist)