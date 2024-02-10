# 47deathsaves.py by George Mo, Ethan Djou, Khalid Saif

import random

deaths = 0
stabilizations = 0
revives = 0
trials = 10000
for i in range(trials):
	successes = 0
	failures = 0
	while successes < 3 and failures < 3:
		roll = random.randint(1, 20)
		if roll == 1:
			failures += 2
		elif 1 < roll < 10:
			failures += 1
		elif 10 <= roll < 20:
			successes += 1
		elif roll == 20:
			revives += 1
			break
	if failures >= 3:
		deaths += 1
	if successes == 3:
		stabilizations += 1
prob_death = deaths / trials
prob_stabilizations = stabilizations / trials
prob_revives = revives / trials
print(prob_death, prob_stabilizations, prob_revives)