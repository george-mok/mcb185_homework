# 46savingthrows.py by George Mo, Ethan Djou, Khalid Saif

import random
										#normal, advantage, disadvantage



trials = 1000

for i in range(5, 16, 5):							#advantage dc of 5,10,&15.
	print(i, end='\t')
	success = 0
	for n in range(trials):
		d1 = random.randint(1, 20)
		d2 = random.randint(1, 20)
		if d1 > d2: 
			a = d1
		else: 
			a = d2
		if a >= i:
			success += 1
	print(success / trials)
print('\n')

for i in range(5, 16, 5):							#disadvantage
	print(i, end='\t')
	success = 0
	for n in range(trials):
		d1 = random.randint(1, 20)
		d2 = random.randint(1, 20)
		if d1 < d2:
			a = d1
		else:
			a = d2
		if a >= i:
			success += 1
	print(success / trials)
print('\n')

for i in range(5, 16, 5):						#normal
	print(i, end='\t')
	success = 0
	for n in range(trials):
		d = random.randint(1, 20)
		if d >= i:
			success += 1
	print(success / trials)