# 62skewer.py by George Mo and Jordan Shore

import gzip
import dogma
import sys
import mcb185

path = sys.argv[1]
w    = int(sys.argv[2])

"""
for defline, seq in mcb185.read_fasta(path):
	for i in range(len(seq) - w + 1):
		s = seq[i:i+w]
		#print(f'{i}\t{dogma.gc_comp(s):.3f}\t{dogma.gc_skew(s):.3f}')
"""
	

complist = []
skewlist = []
for defline, seq in mcb185.read_fasta(path):
	fullseq = list(seq)
	window = fullseq[:w]
	gccomp = dogma.gc_comp(window)
	gcskew = dogma.gc_skew(window)
	for i in range(len(seq) - w + 1):
		if i < len(seq) - w:
			window.pop(0)
			window.append(seq[i+w])
		drop   = window[0]
		pickup = window[-1]
		if drop in 'GC':
			gccomp = dogma.gc_comp(window)
			gcskew = dogma.gc_skew(window)
		if pickup in 'GC':
			gccomp = dogma.gc_comp(window)
			gcskew = dogma.gc_skew(window)


"""
seq = 'ACGTACGTGGGGGACGTACGTCCCCC'
w = 10
fullseq = list(seq)
window = list(fullseq[:w])
gccomp = dogma.gc_comp(window)
gcskew = dogma.gc_skew(window)
for i in range(len(seq) - w + 1):
	print(i, gccomp, gcskew)
	if i < len(seq) - w:
		window.pop(0)
		window.append(seq[i+w])
	if window[0]  != 'C' or window[0]  != 'G':
		gccomp = dogma.gc_comp(window)
		gcskew = dogma.gc_skew(window)
	if window[-1] == 'C' or window[-1] == 'G':
		gccomp = dogma.gc_comp(window)
		gcskew = dogma.gc_skew(window)
"""