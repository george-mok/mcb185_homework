# 74genefinder.py by George Mo and Khalid Saif

import sys
import mcb185
import dogma

path = sys.argv[1]
minlength = int(sys.argv[2])

# gene 1: pos 190 to 255; + strand; path = "shortecoligenome"

start_codon = 'ATG'
stop_codons = ['TAA', 'TAG', 'TGA']

def find_orfs(seq, frame, strand):
	orfs = []
	i = 0
	while i < len(seq):
		codon = seq[i:i+3]
		if codon != start_codon: 
			i += 3
			continue
		
		start = i                # record start coordinate
		
		for j in range(i, len(seq) -2, 3):   # read in 3's from start
			codon = seq[j:j+3]
			if codon in stop_codons:
				stop = j + 2     # record stop coordinate
				
				if (stop - start) >= minlength:
					if strand == '+': 
						orfs.append((start + frame + 1, stop + frame + 1, strand))  # +1 since start at i = 0
					else:
						orfs.append((len(seq) - stop, len(seq) - start, strand))
				i = j  # new start pos
				break
		i += 3  # onto next codon
	return orfs

def gff_format(defline, start, end, strand):
	return f'{defline}\tRefSeq\tCDS\t{start}\t{end}\t.\t{strand}'

for defline, seq in mcb185.read_fasta(path):
	for frame in range(3):
		print(f'frame\t{frame}')
		print()
		identifier = defline.split()[0]
		pos_orfs = find_orfs(seq[frame:], frame, '+')
		neg_orfs = find_orfs(dogma.revcomp(seq)[frame:], frame, '-')
		
		for start, end, strand, in pos_orfs:
			print(gff_format(identifier, start, end, strand))
		for start, end, strand in neg_orfs:
			print(gff_format(identifier, start, end, strand))