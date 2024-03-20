# 62skewer.py by George Mo, Jordan S., Ethan D., and Khalid S.

import sys
import mcb185
import dogma

path = sys.argv[1]
w    = int(sys.argv[2])

for defline, seq in mcb185.read_fasta(path):
	g = seq[0:w].count('G')
	c = seq[0:w].count('C')
	for i in range(1, len(seq) - w):
		drop = seq[i]
		pickup = seq[i+w]
	
		if drop == 'C': c -= 1
		if drop == 'G': g -= 1
		if pickup == 'C': c += 1
		if pickup == 'G': g += 1

		comp = (c+g)/w
		if (g+c) > 0: skew = (g-c)/(g+c)
		else:         skew = 0
	
		#print(i, f'gccomp:{comp:.3f}', f'gcskew:{skew:.3f}')


# 61skewer for comparison
"""
for defline, seq in mcb185.read_fasta(path):
	for i in range(len(seq) - w + 1):
		s = seq[i:i+w]
		comp = dogma.gc_comp(s)
		skew = dogma.gc_skew(s)
"""