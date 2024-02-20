# 57birthday.py by George Mo

import random
import sys

trials = int(sys.argv[1])
days   = int(sys.argv[2])
people = int(sys.argv[3])

hits = 0
for i in range(trials):
	calender = []
	for j in range(days+1):
		calender.append(0)
	for k in range(people):
		next_bday = random.randint(1, days)
		if calender[next_bday] == 1:
			hits += 1
			break
		else:
			calender[next_bday] = 1
			
print(hits)
print(f'Probability: {hits / trials}')