# 53genomestats.py by George Mo

import gzip
import sys
import math

gffpath = sys.argv[1]
feature = sys.argv[2]

def minmax(vals):
	mini = vals[0]
	maxi = vals[0]
	for val in vals:
		if val < mini: mini = val
		if val > maxi: maxi = val
	return mini, maxi
	
def mean(vals):
	total = 0
	for val in vals: total += val
	return total / len(vals)

def stdv(vals):
	total = 0
	for val in vals:
		total += (val - mean(vals))**2
	return math.sqrt(total / len(vals))

def median(vals):
	vals.sort()
	if len(vals) % 2 != 0:
		middle = int((len(vals) + 1) / 2)
		return vals[middle]
	else:
		middle1 = int((len(vals) / 2) - 1)
		middle2 = int(len(vals) / 2)
		return int((vals[middle1] + vals[middle2]) / 2)

lengths = []
total_count = 0
with gzip.open(gffpath, 'rt') as fp:
	for line in fp:
		total_count += 1
		words = line.split()
		if words[2] != feature: continue
		beg = int(words[3])
		end = int(words[4])
		lengths.append(end - beg + 1)
	gcount     = (len(lengths))
	gmin, gmax = (minmax(lengths))
	gmean      = mean(lengths)
	gstdv      = stdv(lengths)
	gmedian    = median(lengths)
	gpercent   = (gcount / total_count) * 100

print('Genome Stats:')	
print(f'count: {gcount}')
print(f'min: {gmin}')
print(f'max: {gmax}')
print(f'mean: {gmean}')
print(f'stdv: {gstdv}')
print(f'median: {gmedian}')
print(f'percent: {gpercent}')