# 55colorname.py by George Mo

import sys

colorfile = sys.argv[1]
R = int(sys.argv[2])
G = int(sys.argv[3])
B = int(sys.argv[4])

colorsin = [R, G, B]

def dtc(P, Q):
	d = 0
	for p, q in zip(P, Q):
		d += abs(p - q)
	return d
	
"""
create list of acceptable colors; append list with smallest diff
for scenarios with same magnitude of diff?
"""

with open(colorfile) as fp:
	maxdiff = 765
	match = 0
	for line in fp:
		columns = line.split()
		colorvalues = columns[2].split(',')
		r_comp    = int(colorvalues[0])
		g_comp    = int(colorvalues[1])
		b_comp    = int(colorvalues[2])
		colorcomp = [r_comp, g_comp, b_comp]
		totaldiff = dtc(colorsin, colorcomp)
		if totaldiff < maxdiff:
			maxdiff = totaldiff
			match = columns[0]
				
print(match)