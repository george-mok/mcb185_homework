# 45dndstats.py by George Mo, Ethan Djou, Khalid Saif

import random
import sys

# 3D6

trials = 10000
total = 0
for i in range(trials):
	score = 0
	for j in range(3):
		dice = random.randint(1, 6)
		score += dice
	total += score
avg_3d6 = total / trials
print('3D6:', avg_3d6)


# 3D6r1

trials = 10000
total = 0
for i in range(trials):
	score = 0
	for j in range(3):
		dice = random.randint(1, 6)
		if dice == 1: dice = random.randint(1, 6)
		score += dice
	total += score
avg_3d6r1 = total / trials
print('3D6r1:', avg_3d6r1)

#3D6x2

trials = 10000
total = 0
for i in range(trials):
	score = 0
	for j in range(3):
		dice1 = random.randint(1, 6)
		dice2 = random.randint(1, 6)
		if dice1 > dice2:
			score += dice1
		else:
			score += dice2
	total += score
avg_3d6x2 = total / trials
print('3D6x2:', avg_3d6x2)

# 4D6d1

trials = 10000
total = 0
for i in range(trials):
	score = 0
	d1 = random.randint(1, 6)
	d2 = random.randint(1, 6)
	d3 = random.randint(1, 6)
	d4 = random.randint(1, 6)
	if d1 <= d2 and d1 <= d3 and d1 <= d4:
		score += d2 + d3 + d4
	elif d2 <= d1 and d2 <= d3 and d2 <= d4:
		score += d1 + d3 + d4
	elif d3 <= d1 and d3 <= d2 and d3 <= d4:
		score += d1 + d2 + d4
	else:
		score += d1 + d2 + d3
	total += score
avg_4d6d1 =  total / trials
print('4D6d1:', avg_4d6d1)

# ex. 4 2 2 6; work around dice matching