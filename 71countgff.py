# 71countgff.py

import gzip
import sys

count = {}
with gzip.open(sys.argv[1], 'rt') as fp:
	for line in fp:
		if line.startswith('#'): continue
		f = line.split()
		feature = f[2]
		if feature not in count: count[feature] = 0
		count[feature] += 1
# for f, n in count.items(): print(f, n)
# for k in sorted(count): print(k, count[k]) # sort by keys
for k, v in sorted(count.items(), key = lambda item: item[1]):  # sort by values
	print(k, v)
	
"""
lambda functions
def by_value(tuple):
	return tuple[1]

for k,v in sorted(count.items(), key=by_value):
	print(k, v)
"""