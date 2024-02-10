# 43randomdna.py by George Mo

import random

n = 3 # number of sequences

for i in range(1, n+1):
	print(f'>seq-{i}')
	limit = random.randint(50, 60)
	for i in range(limit):
		print(random.choice('ACGT'), end='')
	print()