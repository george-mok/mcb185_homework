# 64profinder.py by George Mo, Ethan Djou, and Khalid Saif

import dogma
import sys
import mcb185
import gzip

path = sys.argv[1]
min_length = int(sys.argv[2])

def find_orfs(dnaseq, mini):      # open reading frames
	coding_sequences = []
	for orf in dogma.translate(dnaseq).split('*'):
		if 'M' in orf:
			start = orf.find('M')
			protseq = orf[start:]
			if len(protseq) >= min_length:
				coding_sequences.append(protseq)
	return coding_sequences

for defline, seq in mcb185.read_fasta(path):
	words = defline.split()
	name  = words[0]
	reverseq = dogma.revcomp(seq)
	identifier = 0
	for frame in range(3):
		for protein in find_orfs(seq[frame:], min_length):
			identifier += 1
			print(f'>{name}-proto-{identifier}')
			print(protein)
		for revprotein in find_orfs(seq[frame:], min_length):
			identifier += 1
			print(f'>{name}-proto-{identifier}')
			print(revprotein)
	


#seq = 'ATGTCAATGTTTGCTTAAATAGTTGGGTTCATGTAA'
