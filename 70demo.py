# 70demo.py by George Mo

import itertools

d = {'dog': 'woof', 'cat': 'meow'}
d['pig'] = 'oink'

"""
d['cat'] = 'mew'
del d['cat']
if 'dog' in d: print(d['dog'])
"""

# for key in d: print(f'{key} says {d[key]}')
# for k, v in d.items(): print(k, 'says', v)

print(d.keys(), d.values(), list(d.values()))

"""
count = {}            # accounts for unexpected letters in seq
for nt in seq:
	if nt not in count: count[nt] = 0
	count[nt] += 1
"""

for nts in itertools.product('ACGT', repeat=2):
	print(nts)