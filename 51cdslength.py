# 51 cdslength.py by George Mo

import gzip

lengths = []
path = 'ecoli.gff.gz'
with gzip.open(path, 'rt') as fp:
	for line in fp:
		if line[0] == '#': continue
		words = line.split()
		if words[2] != 'CDS': continue
		beg = int(words[3])
		end = int(words[4])
		lengths.append(end - beg + 1)