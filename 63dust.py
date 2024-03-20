# 63dust.py by George Mo

import sys
import mcb185
import math

def entropy(a, c, g, t):
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

path   = sys.argv[1]
w      = int(sys.argv[2])    # window size
h      = float(sys.argv[3])  # entropy threshold

#seq = 'AAAAAAAAAAAAAAAAATCGATCGT'
      # 123456789ABCDEFGHIJKLMNOP

for defline, seq in mcb185.read_fasta(path):
	print('>', defline, sep='')
	a = seq[0:w].count('A')
	c = seq[0:w].count('C')
	g = seq[0:w].count('G')
	t = seq[0:w].count('T')

	newseq = list(seq)

	for i in range(len(seq) -w +1):
		drop = seq[i]
		if i > len(seq) -w +1:
			pickup = seq[i+w]
		else:
			pickup = seq[i-1+w]
		
		if drop == 'A': a -= 1
		if drop == 'C': c -= 1
		if drop == 'G': g -= 1
		if drop == 'T': t -= 1
		if pickup == 'A': a += 1
		if pickup == 'C': c += 1
		if pickup == 'G': g += 1
		if pickup == 'T': t += 1
		
		if entropy(a, c, g, t) <= h:
			for j in range(w):
				newseq[i+j] = 'N'
	maskedseq = ''.join(newseq)
	for i in range(0, len(maskedseq), 60):
		print(maskedseq[i:i+60])