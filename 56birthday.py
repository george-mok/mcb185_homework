# 56birthday.py by George Mo

import random
import sys

trials = int(sys.argv[1])
days   = int(sys.argv[2])
people = int(sys.argv[3])

hits = 0
for i in range(trials):
	bdays = []
	for j in range(people):
		next_bday = random.randint(1, days)
		if next_bday in bdays:
			hits += 1
			break
		else:
			bdays.append(next_bday)
	
print(hits)
print(f'Probability: {hits / trials}')