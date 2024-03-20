# 73missingkmers.py by George Mo

import mcb185
import sys
import itertools
import dogma

fasta = sys.argv[1]

for k in range(1, 10):
	print('checking', k)
	
	# get all kmers for all seq
	kcount = {}
	for defline, seq in mcb185.read_fasta(fasta):
		for i in range(len(seq) -k +1):
			kmer = seq[i:i+k]
			revkmer = dogma.revcomp(seq[i:i+k])
			if kmer not in kcount: kcount[kmer] = 0
			if revkmer not in kcount: kcount[revkmer] = 0
			kcount[kmer] += 1
			kcount[revkmer] += 1
			
	# check all kmers against all possible
	if len(kcount.keys()) == 4**k: continue
	
	# report missing kmers
	for ktup in itertools.product('ACGT', repeat=k):
		kmer = ''.join(ktup)
		if kmer not in kcount: print(kmer)
		
	sys.exit()